from datetime import datetime, date, time
from typing import List, Optional

from pychronic.enums import (
    get_month_for_keyword,
    get_period_for_keyword,
    convert_from_keyword,
    Month,
    Period,
    get_month_number,
)
from pychronic.models.data_types import DataType
from pychronic.models.tagged_word import TaggedWord

int_suffixes = {"st", "nd", "rd", "th"}

data_type_vs_validator = {}

date_month_possible_patterns = ["%Y-%m", "%Y:%m", "%Y/%m"]

date_month_year_possible_patterns = ["%Y-%m-%d", "", "%Y/%m/%d", "%d/%m/%Y", "%d-%m-%Y"]

hour_min_patterns = ["%H:%M:%S", "%H-%M-%S", "%H:%M", "%H-%M"]


class Tagger:
    def __init__(self):
        data_type_vs_validator[DataType.INT] = self._to_int
        data_type_vs_validator[DataType.MONTH] = self._to_month
        data_type_vs_validator[DataType.DATE_MONTH_YEAR] = self._to_date_month_year
        data_type_vs_validator[DataType.PERIOD] = self._to_period
        data_type_vs_validator[DataType.HOUR_MIN_SEC] = self._to_hour_min_sec

    def tag(self, source_text: str = "") -> List[TaggedWord]:
        rv = []
        words = source_text.split(" ")
        for index, val in enumerate(words):
            for k, v in data_type_vs_validator.items():
                stemmed_word = v(words, index)
                if stemmed_word:
                    rv.append(TaggedWord(val, k, stemmed_word))
                    break
            else:
                rv.append(TaggedWord(val, DataType.TEXT, val))

        return rv

    def _to_int(self, words_list: List, index: int) -> Optional[int]:
        word = words_list[index]
        if word.isdigit():
            return int(words_list[index])

        last_chars = word.lower()[-2:]
        if last_chars not in int_suffixes:
            return None

        if word[:-2].isdigit():
            return int(word[:-2])

    def _to_month(self, words_list: List, index: int) -> Optional[Month]:
        word = words_list[index]
        return get_month_for_keyword(word)

    def _to_date_month(self, words_list: List, index: int) -> Optional[datetime]:
        word = words_list[index]
        return self._word_to_date_month(word)

    def _word_to_date_month(self, word):
        for p in date_month_possible_patterns:
            try:
                rv = datetime.strptime(word, p)
                if not rv:
                    new_word = self._replace_month_number(word)
                    if word != new_word:
                        return self._word_to_date_month(new_word)

            except ValueError:
                pass

    def _to_date_month_year(self, words_list: List, index: int) -> Optional[date]:
        word = words_list[index]
        return self._word_to_date_month_year(word)

    def _word_to_date_month_year(self, word):
        for p in date_month_year_possible_patterns:
            try:
                return datetime.strptime(word, p).date()
            except ValueError:
                pass

        rv_datetime = convert_from_keyword(word)
        if not rv_datetime:
            new_word = self._replace_month_number(word)
            if word != new_word:
                return self._word_to_date_month_year(new_word)

        return rv_datetime.date() if rv_datetime else None

    def _to_period(self, words_list: List, index: int) -> Optional[Period]:
        word = words_list[index]
        return get_period_for_keyword(word)

    def _to_hour_min_sec(self, words_list: List, index: int) -> Optional[time]:
        word = words_list[index]
        for p in hour_min_patterns:
            try:
                return datetime.strptime(word, p).time()
            except ValueError:
                pass

    def _replace_month_number(self, word):
        if "-" not in word:
            return word

        rv = []
        splits = word.split("-")
        for s in splits:
            month = get_month_for_keyword(s)
            if month:
                rv.append(str(get_month_number(month)))
                continue
            rv.append(s)
        return "-".join(rv)
