from datetime import datetime, date

from pychronic.datetime_parser import parse
from pychronic.models.parsed_input import MatchedPattern


def test_parser_datetime_and_date():
    input = "Tournament will commence on 12:30 PM on 23rd May and end on 25th aug"
    rv = parse(input)
    curr_year = datetime.now().year
    assert rv.matched_pattern[0] == MatchedPattern(
        from_index=4,
        to_index=8,
        parsed_value=datetime(
            year=curr_year, month=5, day=23, hour=12, minute=30, second=0
        ),
    )
    assert rv.matched_pattern[1] == MatchedPattern(
        from_index=12,
        to_index=13,
        parsed_value=date(year=datetime.now().year, month=8, day=25),
    )


def test_parser_datetime_and_date_period():
    input = "Tournament will commence on 11:30 PM on 23rd May and end on 25th aug"
    curr_year = datetime.now().year
    rv = parse(input)
    assert rv.matched_pattern[0] == MatchedPattern(
        from_index=4,
        to_index=8,
        parsed_value=datetime(
            year=curr_year, month=5, day=23, hour=23, minute=30, second=0
        ),
    )
    assert rv.matched_pattern[1] == MatchedPattern(
        from_index=12,
        to_index=13,
        parsed_value=date(year=datetime.now().year, month=8, day=25),
    )


def test_parser_datetime():
    input = "Today is 25th of december"
    rv = parse(input)
    assert rv.matched_pattern[0] == MatchedPattern(
        from_index=2,
        to_index=4,
        parsed_value=date(year=datetime.now().year, month=12, day=25),
    )


def test_parser_day_month_year():
    input = "Results are on 23-may-2019 or 24-may-2019"
    rv = parse(input)
    assert rv.matched_pattern[0] == MatchedPattern(
        from_index=3,
        to_index=3,
        parsed_value=date(year=datetime.now().year, month=5, day=23),
    )

    assert rv.matched_pattern[1] == MatchedPattern(
        from_index=5,
        to_index=5,
        parsed_value=date(year=datetime.now().year, month=5, day=24),
    )
