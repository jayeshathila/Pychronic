import calendar
from datetime import datetime
from typing import Dict

from pychronic.models.parse_pattern import patterns_to_match

from pychronic.models.parsed_input import ParsedInput, MatchedPattern

from pychronic.enums import get_natural_day_or_none
from pychronic.tagger import Tagger


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


def highlight_from_text(text: str):
    if not text:
        return text

    tagged_words = Tagger().tag(source_text=text)
    rv = ParsedInput([t.word for t in tagged_words])
    index = 0
    while index < len(tagged_words):
        for pattern in patterns_to_match:
            pattern_size = len(pattern.pattern)
            probable_match = tagged_words[index : index + pattern_size]
            if [p.datatype for p in probable_match] == list(pattern.pattern):
                value = pattern.parser(probable_match)
                if value:
                    rv.add_matched_pattern(
                        MatchedPattern(
                            from_index=index,
                            to_index=index + pattern_size - 1,
                            parsed_value=value,
                        )
                    )
                    index += pattern_size - 1
                    break
        index += 1
    return rv


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
