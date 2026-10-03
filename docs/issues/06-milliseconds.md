# Support Unix milliseconds in Timestamp Converter

**Level:** Beginner–intermediate · **Suggested labels:** `help wanted`, `enhancement`

## What to build

Some systems use milliseconds instead of seconds. Add an optional
`unit` parameter accepting `"seconds"` or `"milliseconds"`, defaulting to
`"seconds"`. Do not guess the unit from the size of a number.

## Where to work

- Function: `convert_timestamp` in `src/mcp_tools_lab/tools/timestamps.py`
- Tests: `tests/test_timestamps.py`
- Documentation: `docs/tool-guide.md`

## Examples

- `convert_timestamp("1000", unit="milliseconds")` represents `1970-01-01T00:00:01Z`.
- `convert_timestamp("1970-01-01T00:00:01Z", "to_unix", unit="milliseconds")`
  should include `unix_milliseconds=1000`.

## Acceptance checklist

- [ ] Keep default calls and their result shape unchanged.
- [ ] For millisecond input with `to_iso`, divide by 1000 before converting.
- [ ] When milliseconds are selected, include an additional `unix_milliseconds` field in both directions.
- [ ] Always keep `unix_seconds` in seconds and retain `iso_utc`.
- [ ] Invalid unit names raise a clear `ValueError`.
- [ ] Test 1000 ms, zero, negative values, a fractional second, and an ISO timezone offset.
- [ ] Keep existing timezone, finite-number, and range validation working.
- [ ] Document the new option and examples.

**Hint:** One second equals 1000 milliseconds. Reuse the current conversion path
and convert units at the input/output boundaries.

Run `python -m pytest tests/test_timestamps.py -q`, then `python -m pytest -q`.
