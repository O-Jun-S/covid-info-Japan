import pandas
from datetime import datetime
from datetime import timedelta
from datetime import timezone

JST = timezone(timedelta(hours=+9), 'JST')

POSITIVE_CSV_FILE = "covid_data/positive_data.csv"
DEATH_CSV_FILE = "covid_data/death_data.csv"
PCR_CSV_FILE = "covid_data/pcr_data.csv"
PATIENT_CSV_FILE = "covid_data/patient_data.csv"


class DataControl:
    def __init__(self):
        self.positive_data = pandas.read_csv(POSITIVE_CSV_FILE, encoding="shift_jis")
        self.death_data = pandas.read_csv(DEATH_CSV_FILE, encoding="shift_jis")
        self.pcr_data = pandas.read_csv(PCR_CSV_FILE, encoding="shift_jis")
        self.patient_data = pandas.read_csv(PATIENT_CSV_FILE, encoding="shift_jis")
        self.the_day = None
        self.the_day_key = None
        self.update_date()
    
    def update_date(self):
        self.the_day = datetime.now(JST) - timedelta(days=2)
        self.the_day_key = f"{self.the_day.year}/{self.the_day.month}/{self.the_day.day}"
    
    def get_positive_data(self):
        return int(self.positive_data[self.positive_data["日付"] == self.the_day_key]["PCR 検査陽性者数(単日)"])
    
    def get_death_data(self):
        before_the_day = (self.the_day - timedelta(days=1))
        before_the_day_key = f"{before_the_day.year}/{before_the_day.month}/{before_the_day.day}"

        the_day_death = int(self.death_data[self.death_data["日付"] == self.the_day_key]["死亡者数"])
        the_day_before_yesterday_death = int(self.death_data[self.death_data["日付"] == before_the_day_key]["死亡者数"])
        return the_day_death - the_day_before_yesterday_death
    
    def get_pcr_data(self):
        pcr_num = int(self.pcr_data[self.pcr_data["日付"] == self.the_day_key]["PCR 検査実施件数(単日)"])
        return pcr_num
    
    def get_patient_data(self):
        patient_num = int(self.patient_data[self.patient_data["日付"] == self.the_day_key]["入院治療を要する者"])
        return patient_num

if __name__ == "__main__":
    dc = DataControl()
    print(dc.get_death_data())
    print(dc.get_patient_data())
    print(dc.get_positive_data())
    print(dc.get_pcr_data())
