from datetime import datetime, timedelta, date

from pychronic.models.parsed_input import MatchedPattern

from pychronic.utils import to_natural_time, highlight_from_text


def test_natural_time_conversion_today():
    subject_datetime = datetime.now()
    result = to_natural_time(datetime=subject_datetime)
    assert "today" == result["day"]
    assert subject_datetime.strftime("%B") == result["month"]
    assert subject_datetime.year == result["year"]


def test_natural_time_conversion_yesterday():
    subject_datetime = datetime.now() - timedelta(days=1)
    result = to_natural_time(datetime=subject_datetime)
    assert "yesterday" == result["day"]
    assert subject_datetime.strftime("%B") == result["month"]
    assert subject_datetime.year == result["year"]


def test_natural_time_conversion_tomorrow():
    subject_datetime = datetime.now() + timedelta(days=1)
    result = to_natural_time(datetime=subject_datetime)
    assert "tomorrow" == result["day"]
    assert subject_datetime.strftime("%B") == result["month"]
    assert subject_datetime.year == result["year"]


def test_natural_time_conversion():
    subject_datetime = datetime(year=2019, month=1, day=1, hour=1, minute=0, second=0)
    result = to_natural_time(datetime=subject_datetime)
    assert "1st" == result["day"]
    assert subject_datetime.strftime("%B") == result["month"]
    assert subject_datetime.year == result["year"]


def test_parser_datetime_and_date():
    input = "Tournament will commence on 12:30 PM on 23rd May and end on 25th aug"
    rv = highlight_from_text(input)
    curr_year = datetime.now().year
    assert (
        rv["matched_pattern"][0]
        == MatchedPattern(
            from_index=4,
            to_index=8,
            parsed_value=datetime(
                year=curr_year, month=5, day=23, hour=12, minute=30, second=0
            ),
        ).to_dict()
    )
    assert (
        rv["matched_pattern"][1]
        == MatchedPattern(
            from_index=12,
            to_index=13,
            parsed_value=date(year=datetime.now().year, month=8, day=25),
        ).to_dict()
    )


def test_parser_datetime_and_date_period():
    input = "Tournament will commence on 11:30 PM on 23rd May and end on 25th aug"
    curr_year = datetime.now().year
    rv = highlight_from_text(input)
    assert (
        rv["matched_pattern"][0]
        == MatchedPattern(
            from_index=4,
            to_index=8,
            parsed_value=datetime(
                year=curr_year, month=5, day=23, hour=23, minute=30, second=0
            ),
        ).to_dict()
    )
    assert (
        rv["matched_pattern"][1]
        == MatchedPattern(
            from_index=12,
            to_index=13,
            parsed_value=date(year=datetime.now().year, month=8, day=25),
        ).to_dict()
    )


def test_parser_datetime():
    input = "Today is 25th of december"
    rv = highlight_from_text(input)
    assert (
        rv["matched_pattern"][0]
        == MatchedPattern(
            from_index=2,
            to_index=4,
            parsed_value=date(year=datetime.now().year, month=12, day=25),
        ).to_dict()
    )


def test_parser_day_month_year():
    input = "Results are on 23-may-2019 or 24-may-2019"
    rv = highlight_from_text(input)
    assert (
        rv["matched_pattern"][0]
        == MatchedPattern(
            from_index=3,
            to_index=3,
            parsed_value=date(year=datetime.now().year, month=5, day=23),
        ).to_dict()
    )

    assert (
        rv["matched_pattern"][1]
        == MatchedPattern(
            from_index=5,
            to_index=5,
            parsed_value=date(year=datetime.now().year, month=5, day=24),
        ).to_dict()
    )
