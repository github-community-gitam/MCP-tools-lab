from mcp_tools_lab.tools.csv_tool import inspect_csv


def test_empty_and_header_only():
    assert inspect_csv("")["row_count"] == 0
    assert inspect_csv("name,age")["columns"] == ["name", "age"]


def test_missing_and_ragged_rows():
    result = inspect_csv("name,age\nAda,20\nBob, \nCat\nDan,30,extra")
    assert result["row_count"] == 4
    assert result["missing_values"][1]["count"] == 2
    assert result["inconsistent_rows"] == [
        {"record": 4, "expected": 2, "actual": 1},
        {"record": 5, "expected": 2, "actual": 3},
    ]


def test_quotes_multiline_and_duplicate_headers():
    result = inspect_csv('a,a\n"hello, world","two\nlines"\n,ok')
    assert result["row_count"] == 2
    assert result["missing_values"] == [
        {"column": "a", "index": 0, "count": 1},
        {"column": "a", "index": 1, "count": 0},
    ]


def test_malformed_csv():
    assert inspect_csv('name\n"unfinished')["valid"] is False
