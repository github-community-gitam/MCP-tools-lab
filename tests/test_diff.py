from mcp_tools_lab.tools.diff import compare_text


def test_replacement():
    result = compare_text("hello\nold", "hello\nnew\nextra")
    assert result["added_lines"] == 2
    assert result["removed_lines"] == 1
    assert "-old" in result["diff"]
    assert "+new" in result["diff"]


def test_equal_empty_and_newlines():
    assert compare_text("", "")["diff"] == ""
    assert compare_text("same\r\n", "same")["diff"] == ""
    assert compare_text("", "new")["added_lines"] == 1
    assert compare_text("old", "")["removed_lines"] == 1


def test_unchanged_lines_for_replacement():
    result = compare_text("hello\nold", "hello\nnew")
    assert result["unchanged_lines"] == 1
    assert result["added_lines"] == 1
    assert result["removed_lines"] == 1


def test_unchanged_lines_identical_and_empty():
    assert compare_text("one\ntwo", "one\ntwo")["unchanged_lines"] == 2
    assert compare_text("", "")["unchanged_lines"] == 0


def test_unchanged_lines_entirely_different():
    assert compare_text("old", "new")["unchanged_lines"] == 0


def test_unchanged_lines_ignores_line_endings_and_final_newline():
    assert compare_text("same\r\n", "same")["unchanged_lines"] == 1


def test_unchanged_lines_with_repeated_lines():
    result = compare_text("a\nb\nb\nc", "a\nb\nc\nc")
    assert result["unchanged_lines"] + result["added_lines"] == 4
    assert result["unchanged_lines"] + result["removed_lines"] == 4
    assert result["unchanged_lines"] == 3
