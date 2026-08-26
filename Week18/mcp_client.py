import asyncio

from mcp import Client, StdioServerParameters
from mcp.client.stdio import stdio_client


# Define how our MCP client should start the Hound MCP server.
hound_server = StdioServerParameters(
    command="hound",
)


# Define how our MCP client should start the SQLite MCP server.
# npx runs the server and passes it our local SQLite database.
sqlite_server = StdioServerParameters(
    command="npx",
    args=["-y", "mcp-sqlite", "books.db"],
)


async def main():
    # Connect to the SQLite MCP server.
    async with Client(stdio_client(sqlite_server)) as sqlite_client:

        tools = await sqlite_client.list_tools()

        print("SQLite tools:")
        for tool in tools.tools:
            print(tool.name)
            print(tool.input_schema)


        # Insert one real book record into the books table.
        result = await sqlite_client.call_tool(
            "create_record",
            arguments={
                "table": "books",
                "data": {
                    "upc": "a897fe39b1053632",
                    "title": "A Light in the Attic",
                    "product_type": "Books",
                    "price_excl_tax": 51.77,
                    "price_incl_tax": 51.77,
                    "tax": 0.00,
                    "availability": "In stock (22 available)",
                    "reviews_count": 0,
                    "url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
                },
            },
        )

        # Print the result returned by SQLite.
        print("INSERT result:")
        print(result)

        # Read the inserted record back from the database.
        result = await sqlite_client.call_tool(
            "query",
            arguments={
                "sql": "SELECT * FROM books"
            },
        )

        # Print the stored record to verify the INSERT.
        print("\nStored books:")
        print(result)

        
    
    


if __name__ == "__main__":
    asyncio.run(main())