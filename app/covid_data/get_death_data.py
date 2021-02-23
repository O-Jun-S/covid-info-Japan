import requests

ENDPOINT = "https://www.mhlw.go.jp/content/death_total.csv"
CSV_FILE = "death_data.csv"


class GetDeathData:
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
    get_death_data = GetDeathData()
    get_death_data.get_data()
    get_death_data.write_data()
