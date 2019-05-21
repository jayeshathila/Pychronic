from datetime import datetime, timedelta

from pychronic.utils import to_natural_time


def test_natural_time_conversion_today():
    subject_datetime = datetime.now()
    result = to_natural_time(datetime=subject_datetime)
    assert "today" == result.day
    assert subject_datetime.strftime("%B") == result.month
    assert subject_datetime.year == result.year


def test_natural_time_conversion_yesterday():
    subject_datetime = datetime.now() - timedelta(days=1)
    result = to_natural_time(datetime=subject_datetime)
    assert "yesterday" == result.day
    assert subject_datetime.strftime("%B") == result.month
    assert subject_datetime.year == result.year


def test_natural_time_conversion_tomorrow():
    subject_datetime = datetime.now() + timedelta(days=1)
    result = to_natural_time(datetime=subject_datetime)
    assert "tomorrow" == result.day
    assert subject_datetime.strftime("%B") == result.month
    assert subject_datetime.year == result.year
