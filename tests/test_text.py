from mcp_tools_lab.tools.text import analyze_text


def test_empty_text():
    assert analyze_text("") == {"characters": 0, "words": 0, "lines": 0,
                                "sentences": 0, "frequent_words": []}


def test_words_and_lines():
    result = analyze_text("Hello, hello!\nDon't stop.")
    assert result["words"] == 4
    assert result["lines"] == 2
    assert result["sentences"] == 2
    assert result["frequent_words"][0] == {"word": "hello", "count": 2}


def test_unicode_and_trailing_newline():
    result = analyze_text("café café\n")
    assert result["words"] == 2
    assert result["lines"] == 1
