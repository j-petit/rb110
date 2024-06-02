import pandas as pd
import yaml

def getZugfinderData(date, start, destination, raw_cookie=""):
    """Pulls the data from zugfinder

        Parameters
        ----------
        date : datetime.date
        start : str
        destination : str

        Returns
        -------
        data : pandas.DataFrame

    """
    if raw_cookie:
        headers = {"cookie": raw_cookie}
    else:
        headers = {}

    request = [
               "http://zugfinder.net/en/directconnection",
               start,
               destination,
               date.strftime("%Y%m%d"),
               "0000",
               "Regio"
              ]
    request_full = "-".join(request)
    data = pd.read_html(request_full, flavor="lxml", storage_options=headers)[0]
    data.columns = ['train_no', 'departure_station', 'departure', 'arrival_station', 'arrival', 'connection']
    data.drop(columns='connection', inplace=True)
    data.insert(5, "departure_date", date)
    data['train_no'] = data['train_no'].str.replace(r'\D+', '', regex=True).astype('int')

    # clean out dirty data
    data.drop_duplicates(subset=['train_no'], inplace=True)
    mask = data['train_no'] == 110
    data = data[~mask]
    mask = data['departure'].str.contains('cancelled')
    data = data[~mask]

    # parse delay
    #repl = lambda m: m.group(0)
    #data['delay'] = data['arrival'].str.replace(r'\+([0-9])', repl, regex=True).astype('string')

    return data

def writeDataToDB(data, engine):
    data.to_sql('travelledTrains', engine, if_exists='append', index=False)

def configLoad(path="./config.yaml"):
    with open(path,"r") as file_object:
        config = yaml.load(file_object,Loader=yaml.SafeLoader)
    return config
