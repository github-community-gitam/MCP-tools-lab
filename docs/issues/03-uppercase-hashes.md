# Add an uppercase hash option

**Level:** Beginner · **Suggested labels:** `good first issue`, `enhancement`

## What to build

Hash Generator returns lowercase hexadecimal text. Add an optional
`uppercase: bool = False` parameter to return uppercase when requested.

## Where to work

- Function: `hash_text` in `src/mcp_tools_lab/tools/hashing.py`
- Tests: `tests/test_hashing.py`
- Documentation: `docs/tool-guide.md`

## Example

`hash_text("abc", uppercase=True)` should return a digest starting with `BA7816BF`.
`hash_text("abc")` should still start with `ba7816bf`.

## Acceptance checklist

- [ ] Add the optional typed parameter without changing the default behavior.
- [ ] Uppercase changes only the digest string, not the algorithm name.
- [ ] Support all three existing algorithms.
- [ ] Test default output, uppercase output, and empty text.
- [ ] Update the docstring and guide with one example.

**Hint:** Python strings have an `.upper()` method. Calculate the digest once,
then choose whether to convert it.

Run `python -m pytest tests/test_hashing.py -q`, then `python -m pytest -q`.
