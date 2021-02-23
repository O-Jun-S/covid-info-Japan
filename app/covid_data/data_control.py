import pandas
from datetime import datetime
from datetime import timedelta
from datetime import timezone

JST = timezone(timedelta(hours=+9), 'JST')

POSITIVE_CSV_FILE = "positive_data.csv"
DEATH_CSV_FILE = "death_data.csv"
PCR_CSV_FILE = "pcr_data.csv"
PATIENT_CSV_FILE = "patient_data.csv"


class DataControl:
    def __init__(self):
        self.positive_data = pandas.read_csv(POSITIVE_CSV_FILE)
        self.death_data = pandas.read_csv(DEATH_CSV_FILE)
        self.pcr_data = pandas.read_csv(PCR_CSV_FILE)
        self.patient_data = pandas.read_csv(PATIENT_CSV_FILE)
        self.the_day = None
        self.the_day_key = None
        self.update_date()
    
    def update_date(self):
        self.the_day = datetime.now(JST) - timedelta(days=1)
        self.the_day_key = self.the_day.strftime("%Y/%-m/%-d")
    
    def get_positive_data(self):
        return int(self.positive_data[self.positive_data["日付"] == self.the_day_key]["PCR 検査陽性者数(単日)"])
    
    def get_death_data(self):
        before_the_day_key = (self.the_day - timedelta(days=1)).strftime("%Y/%-m/%-d")
        the_day_death = int(self.death_data[self.death_data["日付"] == self.the_day_key]["死亡者数"])
        the_day_before_yesterday_death = int(self.death_data[self.death_data["日付"] == before_the_day_key]["死亡者数"])
        return the_day_death - the_day_before_yesterday_death
    
    def get_pcr_data(self):
        pcr_num = int(self.pcr_data[self.pcr_data["日付"] == self.the_day_key]["PCR 検査実施件数(単日)"])
        return pcr_num
    
    def get_patient_data(self):
        patient_num = int(self.patient_data[self.patient_data["日付"] == self.the_day_key]["入院治療を要する者"])
        return patient_num
