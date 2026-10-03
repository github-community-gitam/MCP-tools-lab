# MCP Tools Lab

**Seven local developer tools. One Python MCP server.**

MCP Tools Lab brings everyday text and data utilities into a single MCP server.
Format JSON, inspect CSV, compare text, generate hashes, convert timestamps,
and inspect URLs from an MCP client or directly from Python.
Every tool runs locally: no API keys, AI models, paid services, or outbound requests.
Internet access is needed only to download dependencies during setup.

MCP (Model Context Protocol) lets a compatible application discover and call tools.
This project exposes all seven through one local standard-input/output server.
You can also call the Python functions directly, without an MCP client or model.

## The seven tools

1. **`analyze_text`** — count characters, words, lines, approximate sentences, and the ten most frequent words.
2. **`process_json`** — validate, pretty-print, or minify JSON; optionally sort keys.
3. **`inspect_csv`** — show headers, data-row counts, missing values, and inconsistent row lengths.
4. **`hash_text`** — create SHA-256, SHA-512, or BLAKE2b hashes of UTF-8 text.
5. **`compare_text`** — generate a unified line diff and count added and removed lines.
6. **`convert_timestamp`** — convert Unix seconds and timezone-aware ISO 8601 dates.
7. **`inspect_url`** — split a URL into its components without visiting it.

## Quick start

Install Python 3.10 or newer and Git. Then:

```sh
git clone https://github.com/github-community-gitam/MCP-tools-lab.git
cd MCP-tools-lab
python -m venv .venv
```

Activate your environment:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```sh
# macOS / Linux
source .venv/bin/activate
```

If Windows blocks activation, use `.venv\Scripts\python.exe` instead of `python`
in the following commands; changing your execution policy is unnecessary.
On systems where the command is `python3`, use that to create the environment.

```sh
python -m pip install .
python examples/try_tools.py
```

## Connect an MCP client

Run the server with `python -m mcp_tools_lab` or `mcp-tools-lab`.
It waits for MCP messages on standard input; a quiet terminal is normal.
Stop a manually started server with Ctrl+C. Usually your MCP client starts it for you.

For clients that accept an `mcpServers` configuration, use this example and replace
the executable with the **absolute path** to your virtual environment's Python:

```json
{
  "mcpServers": {
    "mcp-tools-lab": {
      "command": "C:/path/to/MCP-tools-lab/.venv/Scripts/python.exe",
      "args": ["-m", "mcp_tools_lab"]
    }
  }
}
```

On macOS/Linux, the executable is `/absolute/path/to/MCP-tools-lab/.venv/bin/python`.
Client configuration locations vary; use your client's local stdio server settings.
The project uses the [official Python MCP SDK's v1 API](https://py.sdk.modelcontextprotocol.io/v1/)
and bounds its dependency below v2 to avoid incompatible API changes.

## Try tools with ordinary Python

```python
from mcp_tools_lab.tools.json_tool import process_json
from mcp_tools_lab.tools.timestamps import convert_timestamp

print(process_json('{"b":2,"a":1}', sort_keys=True))
print(convert_timestamp("0"))
# {'unix_seconds': 0.0, 'iso_utc': '1970-01-01T00:00:00Z'}
```

See [examples/try_tools.py](examples/try_tools.py) for all seven functions and
[docs/tool-guide.md](docs/tool-guide.md) for inputs, results, and edge cases.

## Project layout

```text
src/mcp_tools_lab/
    server.py           # Registers the seven tools
    tools/              # One small Python module per tool
tests/                  # Tool tests and a real MCP round-trip test
examples/try_tools.py   # Run all tools without a model or MCP client
docs/tool-guide.md      # Input/output behavior
```

All application, example, and test code is Python. TOML and Markdown provide
packaging configuration and documentation; no JavaScript or frontend is required.
Tools accept supplied strings, do not read arbitrary files, and process inputs in
memory. The server is designed for local use with small text inputs.

## License

This project is released under the [MIT License](LICENSE).

## Contributors

- [Kush Aggarwal](https://github.com/kushagarwal2910-lang)
- [Driti Gudla](https://github.com/DritiG)
