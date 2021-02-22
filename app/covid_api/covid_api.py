import requests
from datetime import datetime
from datetime import timedelta

ENDPOINT = "https://covid19-japan-web-api.now.sh/api/v1/total"
PARAMETER = {
  "history": "true"
}

class CovidApi:
    def __init__(self):
      self.json_data = None
    
    def get_json_data(self):
        response = requests.get(ENDPOINT, params=PARAMETER)
        self.json_data = response.json()
    
    def get_positive_data(self):
      yesterday = datetime.now() - timedelta(days=1)
      day_bef_yes = yesterday - timedelta(days=1)

      yesterday_key = int(yesterday.strftime("%Y%m%d"))
      day_bef_yes_key = int(day_bef_yes.strftime("%Y%m%d"))

      yesterday_data = None
      day_bef_yes_data = None
      for day in self.json_data:
          if day["date"] == yesterday_key:
              yesterday_data = day
          
          if day["date"] == day_bef_yes_key:
              day_bef_yes_data = day
      
      yesterday_positive = yesterday_data["positive"]
      day_bef_yes_positive = day_bef_yes_data["positive"]
      return yesterday_positive - day_bef_yes_positive
