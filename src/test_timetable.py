
import pytest
import yaml
from timetable import Timetable
from datetime import date


@pytest.fixture
def testTimetable():
    with open('./timetable_leipzig.yaml', 'r') as file:
        configuration = yaml.safe_load(file)
    print(configuration)
    return Timetable(configuration)

def test_Timetable(testTimetable):
    test_date_weekday = date(2024, 5, 22)
    test_date_weekend = date(2024, 5, 19)
    test_date_public_holiday = date(2024, 1, 1)
    assert testTimetable.returnNoTrains(test_date_weekday) == 29
    assert testTimetable.returnNoTrains(test_date_weekend) == 20
    assert testTimetable.returnNoTrains(test_date_public_holiday) == 20
