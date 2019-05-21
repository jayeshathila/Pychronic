from enum import Enum
from typing import Optional


class NaturalDays(Enum):
    YESTERDAY = ("yesterday", -1)
    TODAY = ("today", 0)
    TOMORROW = ("tomorrow", 1)


index_vs_natural_days = {n.value[1]: n.value[0] for n in NaturalDays}


def get_natural_day_or_none(day_index: int) -> Optional[str]:
    return index_vs_natural_days.get(day_index)
