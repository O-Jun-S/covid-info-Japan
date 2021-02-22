import pandas
from datetime import datetime
from datetime import timedelta

POSITIVE_CSV_FILE = "positive_data.csv"


class DataControl:
    def __init__(self):
        self.positive_data = pandas.read_csv(POSITIVE_CSV_FILE)
        self.yesterday = None
        self.yesterday_key = None
        self.update_date()
    
    def update_date(self):
        self.yesterday = datetime.now() - timedelta(days=1)
        self.yesterday_key = self.yesterday.strftime("%Y/%-m/%-d")
    
    def get_positive_data(self):
        return int(self.positive_data[self.positive_data["日付"] == self.yesterday_key]["PCR 検査陽性者数(単日)"])
