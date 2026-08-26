import asyncio

from ollama import chat
from mcp import Client, StdioServerParameters
from mcp.client.stdio import stdio_client


# Define how our MCP client should start the Hound server.
hound_server = StdioServerParameters(
    command="hound",
)


# Define how our MCP client should start the SQLite MCP server.
sqlite_server = StdioServerParameters(
    command="npx",
    args=["-y", "mcp-sqlite", "books.db"],
)


async def main():

    # Store the conversation between the user and Qwen.
    messages = [
        {
            "role": "system",
            "content": (
                "You are an agent. "
                "When the task requires using a tool, "
                "do not provide a final answer until "
                "the required tool calls have been completed."
                "If a tool returns an error, analyze the error, "
                "correct your tool arguments, and try the tool again. "
                "Do not ask the user for permission to fix a tool error."
            ),
        },
        {
            "role": "user",
            "content": (
                "Fetch the book page at "
                "https://books.toscrape.com/catalogue/"
                "a-light-in-the-attic_1000/index.html, "
                "extract the book information, and create a record "
                "in the `books` table using the `create_record` tool. "
                "Do not stop until the record has been created."
            ),
        },
    ]

    # Connect to both MCP servers.
    async with (
        Client(stdio_client(hound_server)) as hound_client,
        Client(stdio_client(sqlite_server)) as sqlite_client,
    ):

        # Get tools from Hound.
        hound_tools_result = await hound_client.list_tools()

        # Get tools from SQLite.
        sqlite_tools_result = await sqlite_client.list_tools()

        # Create one combined list of tools for Qwen.
        ollama_tools = []

        # Add Hound tools.
        for tool in hound_tools_result.tools:
            ollama_tools.append(
                {
                    "type": "function",
                    "function": {
                        "name": tool.name,
                        "description": tool.description,
                        "parameters": tool.input_schema,
                    },
                }
            )

        # Add SQLite tools.
        for tool in sqlite_tools_result.tools:
            ollama_tools.append(
                {
                    "type": "function",
                    "function": {
                        "name": tool.name,
                        "description": tool.description,
                        "parameters": tool.input_schema,
                    },
                }
            )

        print("Available tools:")
        for tool in ollama_tools:
            print("-", tool["function"]["name"])

        # Keep asking Qwen what to do until it gives a final answer.
        while True:

            # Ask Qwen what to do next.
            response = chat(
                model="qwen2.5:7b",
                messages=messages,
                tools=ollama_tools,
            )

            # Add Qwen's response to the conversation history.
            messages.append(response.message)

            # If Qwen does not request a tool, it is ready to answer.
            if not response.message.tool_calls:
                break

            # Get the first tool call requested by Qwen.
            tool_call = response.message.tool_calls[0]

            # Get the tool name chosen by Qwen.
            tool_name = tool_call.function.name

            # Get the arguments chosen by Qwen.
            tool_arguments = tool_call.function.arguments

            print("\nQwen selected tool:")
            print(tool_name)

            print("Arguments:")
            print(tool_arguments)

            # If Qwen selected a Hound tool, execute it through Hound.
            if tool_name in [tool.name for tool in hound_tools_result.tools]:

                tool_result = await hound_client.call_tool(
                    tool_name,
                    arguments=tool_arguments,
                )

            # If Qwen selected a SQLite tool, execute it through SQLite.
            elif tool_name in [tool.name for tool in sqlite_tools_result.tools]:

                tool_result = await sqlite_client.call_tool(
                    tool_name,
                    arguments=tool_arguments,
                )

            else:
                raise ValueError(f"Unknown tool: {tool_name}")

            print("Tool result:")
            print(tool_result)

            # Extract the actual text from the MCP result.
            tool_text = tool_result.content[0].text

            # Give the tool result back to Qwen.
            messages.append(
                {
                    "role": "tool",
                    "tool_name": tool_name,
                    "content": tool_text,
                }
            )

        # Print Qwen's final answer.
        print("\nFinal Qwen response:")
        print(response.message)


if __name__ == "__main__":
    asyncio.run(main())