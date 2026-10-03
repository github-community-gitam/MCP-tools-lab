import pytest
from mcp_tools_lab.tools.hashing import hash_text


def test_sha256_known_vector():
    assert hash_text("abc")["digest"] == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"


@pytest.mark.parametrize("algorithm,length", [("sha256", 64), ("sha512", 128), ("blake2b", 128)])
def test_algorithms(algorithm, length):
    result = hash_text("", algorithm)
    assert len(result["digest"]) == length
    assert result["digest"] == result["digest"].lower()


def test_unsupported_algorithm():
    with pytest.raises(ValueError, match="algorithm"):
        hash_text("abc", "md5")
