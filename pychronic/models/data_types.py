from enum import Enum


class DataType(Enum):
    INT = "int"
    DATE_OF_MONTH = "date"
    DATE_MONTH = "date_month"
    MONTH = "month"
    DATE_MONTH_YEAR = "date_month_year"
    HOUR_MIN_SEC = "hour_min_sec"
    PERIOD = "period"
    TIME = "time"
    TEXT = "text"
