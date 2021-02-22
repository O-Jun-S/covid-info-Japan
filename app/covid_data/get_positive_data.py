import requests


ENDPOINT = "https://www.mhlw.go.jp/content/pcr_positive_daily.csv"
CSV_FILE = "positive_data.csv"


class GetPositiveData:
    def __init__(self):
        self.data = ""
    
    def get_data(self):
        res = requests.get(ENDPOINT)
        res.encoding = res.apparent_encoding
        self.data = res.text

    def write_data(self):
        with open(CSV_FILE, "w") as f:
            f.write(self.data)
