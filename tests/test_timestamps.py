import pytest
from mcp_tools_lab.tools.timestamps import convert_timestamp


def test_epoch_and_offset():
    assert convert_timestamp("0")["iso_utc"] == "1970-01-01T00:00:00Z"
    assert convert_timestamp("1970-01-01T05:30:00+05:30", "to_unix")["unix_seconds"] == 0


def test_fractional_and_negative_seconds():
    assert convert_timestamp("-0.5")["iso_utc"] == "1969-12-31T23:59:59.500000Z"
    assert convert_timestamp("1970-01-01T00:00:00.500000Z", "to_unix")["unix_seconds"] == 0.5


@pytest.mark.parametrize("value,direction", [("nan", "to_iso"), ("inf", "to_iso"),
    ("1e99", "to_iso"), ("oops", "to_iso"), ("2026-01-01", "to_unix"),
    ("2026-01-01T12:00:00", "to_unix"), ("0", "wrong")])
def test_invalid_input(value, direction):
    with pytest.raises(ValueError, match="Cannot convert"):
        convert_timestamp(value, direction)


def test_weekday_utc_for_known_days():
    assert convert_timestamp("0")["weekday_utc"] == "Thursday"
    assert convert_timestamp("345600")["weekday_utc"] == "Monday"
    assert convert_timestamp("1970-01-04T00:00:00Z", "to_unix")["weekday_utc"] == "Sunday"


def test_weekday_utc_uses_utc_not_the_inputs_local_date():
    result = convert_timestamp("1970-01-02T00:30:00+01:00", "to_unix")
    assert result["iso_utc"] == "1970-01-01T23:30:00Z"
    assert result["weekday_utc"] == "Thursday"


def test_weekday_utc_for_negative_timestamp():
    assert convert_timestamp("-0.5")["weekday_utc"] == "Wednesday"


def test_weekday_utc_in_both_directions():
    assert convert_timestamp("0")["weekday_utc"] == convert_timestamp("1970-01-01T00:00:00Z", "to_unix")["weekday_utc"]
