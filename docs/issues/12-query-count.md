# Count URL query parameter entries

**Level:** Beginner · **Suggested labels:** `good first issue`, `enhancement`

## What to build

Add `query_parameter_count` to URL Inspector. Count individual values, including
repeated keys and empty values, rather than just counting unique parameter names.

## Where to work

- Function: `inspect_url` in `src/mcp_tools_lab/tools/urls.py`
- Tests: `tests/test_urls.py`
- Documentation: `docs/tool-guide.md`

## Example

`inspect_url("https://example.com?tag=python&tag=mcp&empty=")` should return
`query_parameter_count=3`, while preserving the current `query_parameters` dictionary.

## Acceptance checklist

- [ ] Count entries from the already parsed query dictionary, summing value-list lengths.
- [ ] A URL with no query or an empty query returns zero.
- [ ] Repeated keys and blank values each count as entries.
- [ ] Follow the existing parser for bare keys (`?flag` counts as one).
- [ ] Encoded separators inside a value do not create extra entries: `?q=a%26b` counts as one.
- [ ] Ignore fragments and preserve all existing output fields and validation.
- [ ] Add tests, update exact-output assertions, and document the new field.

**Hint:** The dictionary values are lists. Add their lengths; do not manually split
the raw URL on `&` or `=`. No network request is needed.

Run `python -m pytest tests/test_urls.py -q`, then `python -m pytest -q`.
