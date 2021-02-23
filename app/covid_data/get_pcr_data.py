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

if __name__ == "__main__":
    get_pcr_data = GetPcrData()
    get_pcr_data.get_data()
    get_pcr_data.write_data()
