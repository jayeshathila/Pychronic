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
