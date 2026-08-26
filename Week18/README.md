# Week 18 — MCP + Agents

## Goal

Build an AI agent that uses multiple MCP servers to retrieve data from a website and store it in a local SQLite database.

The project demonstrates MCP client/server communication, LLM tool selection, multi-step agent orchestration, and error handling.

---

## What is MCP?

MCP (Model Context Protocol) is an open protocol that allows an AI application or agent to connect to external tools and data sources through a standardized interface.

In this project, the MCP client connects the agent to multiple MCP servers.

---

## Architecture

```text
User
  ↓
Agent / Orchestrator
  ↓
LLM (Ollama / Qwen)
  ↓
MCP Client
  ↓
┌───────────────────────┐
│                       │
↓                       ↓
Hound MCP           SQLite MCP
↓                       ↓
Website             Local Database
```

The Agent / Orchestrator is responsible for using the LLM to decide which tool to call next based on the user's goal and the results of previous tool calls.

---

## What we are learning

- MCP client/server communication
- MCP tools
- MCP tool discovery
- LLM tool selection
- Agent orchestration
- Multiple MCP servers
- Error handling
- Logging

---

# MCP Servers

## 1. Hound MCP

**Purpose:** Web research, fetching, crawling and web search.

### Minimum requirements

- Python 3.11+
- `hound-mcp`
- Chromium
- No API key required
- Runs locally

Hound is used to retrieve information from the Books to Scrape website.

---

## 2. mcp-sqlite

**Purpose:** Give the AI agent access to a local SQLite database.

### Minimum requirements

- Python 3.12+
- `uv`
- Local SQLite database
- No API key required

The SQLite MCP server provides tools for reading and modifying the local database.

---

# Key Technologies

## Chromium

**Chromium** is the open-source browser project behind Google Chrome.

In this project, Hound uses Chromium through **Playwright**, a library that allows Hound to control a browser and interact with web pages.

This is useful for websites where content is loaded dynamically with JavaScript.

---

## uv

**uv** is a fast Python package and project manager.

It can be used to:

- create the project's virtual environment;
- install Python packages;
- run Python-based MCP servers.

It is similar to tools such as `pip` and `venv`, but combines several Python environment and package-management functions in one tool.

Example:

```bash
uv venv --python 3.13
```

---

# Hound Installation Status

Hound was installed in the project `.venv`.

Verification:

```bash
hound --doctor
```

Result:

- all health checks passed;
- browser dependencies are installed;
- no API key is required.

---

# Step 1 — MCP Client and Tool Discovery

We created a basic MCP client that connects to the local Hound MCP server.

The client uses the MCP SDK and communicates with Hound through `stdio`.

The first thing the client does is **tool discovery**: it asks Hound which tools are available.

Expected tools include:

- `mcp_smart_fetch`
- `mcp_smart_crawl`
- `mcp_screenshot`
- `mcp_smart_search`
- `cache_clear`
- `version`

This confirms that the MCP client can successfully connect to the Hound server and discover its tools.

---

## Hound MCP — Initial Test

The MCP client successfully connected to Hound and discovered its tools.

We successfully called `mcp_smart_fetch` and retrieved data from Books to Scrape.

`mcp_smart_crawl` discovery returned an empty result for this website, so `mcp_smart_fetch` was used for the scraping test.

This confirms that the MCP connection and tool execution work correctly.

---

# Data Model

We use Hound to collect book information from Books to Scrape.

A single book page returned the following fields:

- `upc` — product identifier
- `title` — book title
- `product_type` — product type
- `price_excl_tax` — price excluding tax
- `price_incl_tax` — price including tax
- `tax` — tax amount
- `availability` — stock information
- `reviews_count` — number of reviews
- `url` — source page URL

---

## SQLite Table

We store these fields in a `books` table:

```text
books

├── upc
├── title
├── product_type
├── price_excl_tax
├── price_incl_tax
├── tax
├── availability
├── reviews_count
└── url
```

The fields above are based on the actual data returned by Hound for a book page.

The decision to store these fields in a SQLite table is a project design choice.

---

# MCP Integration Test

We successfully connected two MCP servers to the same Python MCP client:

- **Hound MCP** — web data retrieval
- **SQLite MCP** — local database operations

## Manual MCP Test

We manually verified that a book record can be inserted into the SQLite database and read back successfully.

Test record:

**A Light in the Attic**

The record contains:

- `upc`
- `title`
- `product_type`
- `price_excl_tax`
- `price_incl_tax`
- `tax`
- `availability`
- `reviews_count`
- `url`

The INSERT operation completed successfully, and a subsequent SELECT returned the stored record.

---

# Agent / LLM Orchestration

The next step was to introduce Qwen as the LLM-based agent.

The agent receives the available tools from the MCP servers and decides which tool to call based on the task and the results returned by previous tool calls.

The Python program acts as the orchestrator between the LLM and the MCP servers.

---

## Agent Flow

```text
User goal
    ↓
Qwen / Agent
    ↓
mcp_smart_fetch
    ↓
Hound MCP
    ↓
Book information
    ↓
Qwen / Agent
    ↓
create_record
    ↓
SQLite MCP
    ↓
books table
```

The agent can perform multiple tool calls as part of a single task.

---

## Tool Selection

Qwen successfully selected:

1. `mcp_smart_fetch` to retrieve the book page.
2. `create_record` to store the extracted information in the `books` table.

The Python orchestrator executes the selected tool and sends the result back to Qwen.

Qwen then decides what to do next.

---

## Error Handling

The agent was also tested with database errors.

When SQLite rejected fields that did not exist in the `books` table, Qwen received the error returned by the MCP tool and retried the operation with modified arguments.

The agent successfully recovered from several consecutive tool errors.

Example sequence:

```text
create_record
    ↓
Error: column "author" does not exist
    ↓
Qwen modifies the arguments
    ↓
create_record
    ↓
Error: column "description" does not exist
    ↓
Qwen modifies the arguments
    ↓
create_record
    ↓
Error: column "number_of_reviews" does not exist
    ↓
Qwen modifies the arguments
    ↓
create_record
    ↓
Record created successfully
```

The final successful operation returned:

```text
Record created successfully
insertedId: 6
```

This demonstrates that the agent can use tool results and error messages to adapt its next action.

---

# Final Result

The project demonstrates:

- MCP client/server communication
- MCP tool discovery
- Multiple MCP servers used by one agent
- LLM-based tool selection
- Multi-step agent orchestration
- Tool error handling and recovery
- Web data retrieval through Hound
- SQLite database operations through MCP
- Successful end-to-end execution of an AI agent

The final agent can retrieve a book page, extract relevant information, select the appropriate database tool, and create a record in the SQLite database.
