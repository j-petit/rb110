import datetime

class Timetable:
    """A simple timetable"""

    count_weekday = 0
    count_weekend = 0
    extras = []

    def __init__(self, timetable):
        self.count_weekday = len(timetable["always"]) + len(timetable["weekday"])
        self.count_weekend = len(timetable["always"]) + len(timetable["weekend"])
        self.extras = timetable["extras"]

    def returnNoTrains(self, request_date):
        if request_date in self.extras:
            return self.count_weekend
        if request_date.weekday() < 5:
            return self.count_weekday
        else:
            return self.count_weekend
