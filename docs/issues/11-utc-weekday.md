# Show the UTC weekday in Timestamp Converter

**Level:** Beginner · **Suggested labels:** `good first issue`, `enhancement`

## What to build

Include `weekday_utc`, an English weekday name, in every successful timestamp result.
Base it on the converted UTC date, not the input's local date or computer timezone.

## Where to work

- Function: `convert_timestamp` in `src/mcp_tools_lab/tools/timestamps.py`
- Tests: `tests/test_timestamps.py`
- Documentation: `docs/tool-guide.md`

## Examples

- Unix `"0"` returns `weekday_utc="Thursday"`.
- `"1970-01-02T00:30:00+01:00"` converts to Thursday in UTC, even though the input's local date is Friday.

## Acceptance checklist

- [ ] Return a full English name, Monday through Sunday, in both conversion directions.
- [ ] Use UTC consistently and do not depend on the machine's language settings.
- [ ] Preserve existing values and error handling.
- [ ] Test known weekdays, a negative timestamp, and an offset that crosses midnight in UTC.
- [ ] If millisecond support has landed, include the field in that mode too.
- [ ] Update exact-result assertions as needed and document the new field.

**Hint:** `date.weekday()` returns 0 for Monday through 6 for Sunday. Use it to
index a fixed list of English names instead of relying on locale-dependent formatting.

Run `python -m pytest tests/test_timestamps.py -q`, then `python -m pytest -q`.
