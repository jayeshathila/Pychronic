import calendar
from datetime import datetime
from typing import Dict

from pychronic.enums import get_natural_day_or_none


def to_natural_time(datetime: datetime, twelve_hour_clock: bool = True) -> Dict:
    day_diff = (datetime.date() - datetime.now().date()).days
    natural_day = get_natural_day_or_none(day_diff)

    if not natural_day:
        day = datetime.date().day
        natural_day = f"{day}{_convert_date_to_str(datetime.date().day)}"

    time_str = datetime.strftime("%I:%M %p" if twelve_hour_clock else "%H:%M")

    return {
        "day": natural_day,
        "time": time_str,
        "month": datetime.strftime("%B"),
        "year": datetime.year,
        "day_of_week": calendar.day_name[datetime.weekday()],
    }


def _convert_date_to_str(day):
    value = str(day)
    if len(value) > 1:
        second_to_last_digit = value[-2]
        if second_to_last_digit == "1":
            return "th"

    last_digit = value[-1]
    if last_digit == "1":
        return "st"
    elif last_digit == "2":
        return "nd"
    elif last_digit == "3":
        return "rd"
    else:
        return "th"
