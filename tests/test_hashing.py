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


def test_uppercase_digest():
    result = hash_text("abc", uppercase=True)
    assert result["digest"] == "BA7816BF8F01CFEA414140DE5DAE2223B00361A396177A9CB410FF61F20015AD"
    assert result["algorithm"] == "sha256"


def test_uppercase_is_optional_and_algorithm_is_unchanged():
    assert hash_text("abc")["digest"].startswith("ba7816bf")
    assert hash_text("abc", uppercase=False) == hash_text("abc")


@pytest.mark.parametrize("algorithm", ["sha256", "sha512", "blake2b"])
def test_uppercase_supports_every_algorithm(algorithm):
    lower = hash_text("abc", algorithm)
    upper = hash_text("abc", algorithm, uppercase=True)
    assert upper["algorithm"] == algorithm
    assert upper["digest"] == lower["digest"].upper()
    assert len(upper["digest"]) == len(lower["digest"])


def test_uppercase_empty_text():
    result = hash_text("", uppercase=True)
    assert result["digest"] == hash_text("", "sha256")["digest"].upper()
    assert result["digest"] == "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855"
