import pytest
from mcp_tools_lab.tools.urls import inspect_url


def test_components_and_repeated_parameters():
    result = inspect_url("https://example.com:8443/path?tag=a&tag=b&empty=&q=hello%20world#part")
    assert result == {"scheme": "https", "hostname": "example.com", "port": 8443,
                      "path": "/path", "query_parameters": {"tag": ["a", "b"], "empty": [""],
                      "q": ["hello world"]}, "fragment": "part"}


def test_ipv6():
    assert inspect_url("http://[::1]:8080")["hostname"] == "::1"


@pytest.mark.parametrize("url", ["example.com", "/path", "https://example.com:99999",
                                  "https://[broken", "https://exa mple.com", "\nhttps://example.com"])
def test_bad_urls(url):
    with pytest.raises(ValueError):
        inspect_url(url)
