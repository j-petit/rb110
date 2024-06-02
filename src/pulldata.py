import sqlalchemy
from datetime import timedelta, datetime
from utilities import getZugfinderData, writeDataToDB, configLoad
import argparse

def mkdate(datestr):
    return datetime.strptime(datestr, '%Y-%m-%d')

default_date = datetime.today() - timedelta(days=1)

parser=argparse.ArgumentParser(description="configure")
parser.add_argument("-s", "--start-date", type=mkdate, default=default_date.strftime('%Y-%m-%d'))
parser.add_argument("-e", "--end-date", type=mkdate, default=default_date.strftime('%Y-%m-%d'))
args=parser.parse_args()

config = configLoad()


engine = sqlalchemy.create_engine(config['database'])
start_date = args.start_date

while start_date <= args.end_date:
    print(start_date)
    data = getZugfinderData(start_date, "Naunhof", "Leipzig_Hbf", config['livedata']['cookie'])
    writeDataToDB(data, engine)
    start_date += timedelta(days=1)
