"""Content hashes; these are not password storage functions."""

import hashlib
from typing import Literal


def hash_text(text: str, algorithm: Literal["sha256", "sha512", "blake2b"] = "sha256", uppercase: bool = False) -> dict:
    """Hash UTF-8 text using SHA-256, SHA-512, or BLAKE2b; return hex.

    The digest is lowercase by default. Pass uppercase=True for an uppercase
    digest; the algorithm name is returned unchanged.
    """
    algorithms = {"sha256": hashlib.sha256, "sha512": hashlib.sha512, "blake2b": hashlib.blake2b}
    if algorithm not in algorithms:
        raise ValueError("algorithm must be sha256, sha512, or blake2b.")
    digest = algorithms[algorithm](text.encode("utf-8")).hexdigest()
    return {"algorithm": algorithm, "digest": digest.upper() if uppercase else digest}
