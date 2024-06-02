import pandas as pd
import sqlalchemy
import yaml
import datetime
from datetime import datetime, timedelta
from timetable import Timetable
from utilities import configLoad
import argparse

def mkdate(datestr):
    return datetime.strptime(datestr, '%Y-%m-%d')

default_date = datetime.today() - timedelta(days=1)

parser=argparse.ArgumentParser(description="configure")
parser.add_argument("-s", "--start-date", type=mkdate, default=default_date.strftime('%Y-%m-%d'))
parser.add_argument("-e", "--end-date", type=mkdate, default=default_date.strftime('%Y-%m-%d'))
args=parser.parse_args()

config = configLoad()

engine = sqlalchemy.create_engine(config["database"])

with open(config['timetable']['file'], 'r') as file:
    configuration = yaml.safe_load(file)

timetable = Timetable(configuration)
def rowFunction(row):
    return timetable.returnNoTrains(row)

dti = pd.date_range(start=args.start_date, end=args.end_date, freq="D")
data = pd.DataFrame(index=dti)
data["planned_trains"] = 0
data["planned_trains"] = data.index.to_series().apply(rowFunction)

data.to_sql('plannedTrains', engine, if_exists='append', index=True)
