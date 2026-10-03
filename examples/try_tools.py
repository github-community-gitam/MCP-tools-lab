"""Run after installing the project: python examples/try_tools.py."""

from pprint import pprint

from mcp_tools_lab.tools.csv_tool import inspect_csv
from mcp_tools_lab.tools.diff import compare_text
from mcp_tools_lab.tools.hashing import hash_text
from mcp_tools_lab.tools.json_tool import process_json
from mcp_tools_lab.tools.text import analyze_text
from mcp_tools_lab.tools.timestamps import convert_timestamp
from mcp_tools_lab.tools.urls import inspect_url


def main() -> None:
    examples = {
        "Text Analyzer": analyze_text("Hello, contributors! Hello, Python."),
        "JSON Toolkit": process_json('{"b":2,"a":1}', sort_keys=True),
        "CSV Inspector": inspect_csv("name,language\nAda,Python\nBob,"),
        "Hash Generator": hash_text("hello"),
        "Text Comparison": compare_text("hello\nold", "hello\nnew"),
        "Timestamp Converter": convert_timestamp("0"),
        "URL Inspector": inspect_url("https://example.com/tools?tag=python&tag=mcp#start"),
    }
    for name, result in examples.items():
        print(f"\n{name}")
        pprint(result)


if __name__ == "__main__":
    main()
