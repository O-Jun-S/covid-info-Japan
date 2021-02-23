import requests

ENDPOINT = "https://www.mhlw.go.jp/content/pcr_tested_daily.csv"
CSV_FILE = "pcr_data.csv"

class GetPcrData:
    def __init__(self):
        self.data = ""

    def get_data(self):
        res = requests.get(ENDPOINT)
        res.encoding = res.apparent_encoding
        self.data = res.text

    def write_data(self):
        with open(CSV_FILE, "w") as f:
            f.write(self.data)
