from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional, List


@dataclass
class NaturalDayValue:
    keywords: List
    index: int


class NaturalDay(Enum):
    YESTERDAY = NaturalDayValue(keywords=["yesterday"], index=-1)
    TODAY = NaturalDayValue(keywords=["today"], index=0)
    TOMORROW = NaturalDayValue(keywords=["tomorrow"], index=1)


index_vs_natural_days = {n.value.index: n.value.keywords for n in NaturalDay}

keyword_vs_natural_day = {
    keyword: n for n in NaturalDay for keyword in n.value.keywords
}


def get_natural_day_or_none(day_index: int) -> Optional[str]:
    return index_vs_natural_days.get(day_index)


def convert_from_keyword(keyword: str) -> Optional[datetime]:
    natural_day = keyword_vs_natural_day.get(keyword)
    if not natural_day:
        return None

    if natural_day == NaturalDay.YESTERDAY:
        return datetime.now() - timedelta(days=1)
    elif natural_day == NaturalDay.TODAY:
        return datetime.now()
    return datetime.now() + timedelta(days=1)


class Month(Enum):
    JANUARY = ("january", "jan")
    FEB = ("february", "feb")
    MARCH = ("march", "mar")
    APRIL = ("april", "apr")
    MAY = ("may",)
    JUNE = ("june", "jun")
    JULY = ("july", "jul")
    AUGUST = ("august", "aug")
    SEPTEMBER = ("september", "sep", "sept")
    OCTOBER = ("october", "oct")
    NOVEMBER = ("november", "nov")
    DECEMBER = ("december", "dec")


keyword_vs_month = {keyword: m for m in Month for keyword in m.value}


def get_month_for_keyword(keyword: str) -> Optional[Month]:
    return keyword_vs_month.get(keyword.lower())


class Period(Enum):
    AM = ("a.m", "am")
    PM = ("p.m", "pm")


keyword_vs_period = {keyword: p for p in Period for keyword in p.value}


def get_period_for_keyword(keyword: str) -> Optional[Month]:
    return keyword_vs_period.get(keyword.lower())
