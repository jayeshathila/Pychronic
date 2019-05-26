from pychronic.models.data_types import DataType
from pychronic.tagger import Tagger


def test_tagger_for_date_time():
    subject = "Will be there at 2:15 pm today"
    tagged_words = Tagger().tag(subject)
    tag_map = {
        "Will": DataType.TEXT,
        "be": DataType.TEXT,
        "there": DataType.TEXT,
        "at": DataType.TEXT,
        "2:15": DataType.HOUR_MIN_SEC,
        "pm": DataType.PERIOD,
        "today": DataType.DATE_MONTH_YEAR,
    }
    assert all(tag_map[t.word] == t.datatype for t in tagged_words)


def test_tagger_for_date_time_and_():
    subject = "Tournament will commence on 12:30 PM on 23rd May and end on 25th aug"
    tagged_words = Tagger().tag(subject)
    tag_map = {
        "Tournament": DataType.TEXT,
        "will": DataType.TEXT,
        "commence": DataType.TEXT,
        "on": DataType.TEXT,
        "12:30": DataType.HOUR_MIN_SEC,
        "PM": DataType.PERIOD,
        "23rd": DataType.INT,
        "May": DataType.MONTH,
        "and": DataType.TEXT,
        "end": DataType.TEXT,
        "25th": DataType.INT,
        "aug": DataType.MONTH,
    }
    assert all(tag_map[t.word] == t.datatype for t in tagged_words)
