# Exposing class to use the fields as per end users convinience
class PychronicDatetime:
    def __init__(self, day: str, time: str, month: str, year: int, day_of_week: str):
        self.day = day
        self.time = time
        self.month = month
        self.year = year
        self.day_of_week = day_of_week

    def __repr__(self):
        return f"{self.day} {self.month} {self.year}, {self.time}"

    def __str__(self):
        return f"{self.day} {self.month} {self.year}, {self.time}"
