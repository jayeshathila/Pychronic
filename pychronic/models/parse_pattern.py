from datetime import datetime, date
from typing import Optional, Tuple

from pychronic.enums import get_month_number, Period
from pychronic.models.data_types import DataType


class PatternVsParser:
    def __init__(self, pattern: Tuple, parser: callable):
        self.pattern = pattern
        self.parser = parser


def _parse_day_month(day: int, month: int) -> Optional[date]:
    try:
        return date(year=datetime.now().year, month=month, day=day)
    except:
        return None


def _parse_datetime(
    year: int, month: int, day: int, hour: int, minute: int, second: int
) -> Optional[datetime]:
    try:
        return datetime(
            year=year, month=month, day=day, hour=hour, minute=minute, second=second
        )
    except:
        return None


# Order matter here
patterns_to_match = [
    PatternVsParser(
        pattern=(
            DataType.HOUR_MIN_SEC,
            DataType.PERIOD,
            DataType.TEXT,
            DataType.INT,
            DataType.MONTH,
        ),
        parser=lambda words: _parse_datetime(
            year=datetime.now().year,
            month=get_month_number(words[-1].stemmed_word),
            day=words[-2].stemmed_word,
            hour=words[0].stemmed_word.hour + 12
            if words[1].stemmed_word == Period.PM
            and words[0].stemmed_word.hour + 12 < 24
            else words[0].stemmed_word.hour,
            minute=words[0].stemmed_word.minute,
            second=words[0].stemmed_word.second,
        )
        if _parse_datetime(
            year=datetime.now().year,
            month=get_month_number(words[-1].stemmed_word),
            day=words[-2].stemmed_word,
            hour=words[0].stemmed_word.hour,
            minute=words[0].stemmed_word.minute,
            second=words[0].stemmed_word.second,
        )
        else None,
    ),
    PatternVsParser(
        pattern=(
            DataType.HOUR_MIN_SEC,
            DataType.PERIOD,
            DataType.TEXT,
            DataType.DATE_MONTH_YEAR,
        ),
        parser=lambda words: datetime(
            year=words[-1].stemmed_word.year,
            month=words[-1].stemmed_word.month,
            day=words[-1].stemmed_word.day,
            hour=words[0].stemmed_word.hour,
            minute=words[0].stemmed_word.minute,
            second=words[0].stemmed_word.second,
        ),
    ),
    PatternVsParser(
        pattern=(DataType.HOUR_MIN_SEC, DataType.TEXT, DataType.DATE_MONTH_YEAR),
        parser=lambda words: datetime(
            year=words[-1].stemmed_word.year,
            month=words[-1].stemmed_word.month,
            day=words[-1].stemmed_word.day,
            hour=words[0].stemmed_word.hour,
            minute=words[0].stemmed_word.minute,
            second=words[0].stemmed_word.second,
        ),
    ),
    PatternVsParser(
        pattern=(DataType.INT, DataType.TEXT, DataType.MONTH),
        parser=lambda words: _parse_day_month(
            words[0].stemmed_word, get_month_number(words[-1].stemmed_word)
        )
        if _parse_day_month(
            words[0].stemmed_word, get_month_number(words[-1].stemmed_word)
        )
        else None,
    ),
    PatternVsParser(
        pattern=(DataType.INT, DataType.MONTH),
        parser=lambda words: _parse_day_month(
            words[0].stemmed_word, get_month_number(words[-1].stemmed_word)
        )
        if _parse_day_month(
            words[0].stemmed_word, get_month_number(words[-1].stemmed_word)
        )
        else None,
    ),
    PatternVsParser(
        pattern=(DataType.DATE_MONTH_YEAR,), parser=lambda words: words[0].stemmed_word
    ),
    PatternVsParser(
        pattern=(DataType.HOUR_MIN_SEC,), parser=lambda words: words[0].stemmed_word
    ),
]
