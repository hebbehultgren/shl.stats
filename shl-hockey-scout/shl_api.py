import requests
class SHLApi:
    def __init__(self):
        self.base_url = "https://www.shl.se/api/statistics-v2/stats-info/players_summary?count=25&ssgtUuid=qa98unlbd6&provider=statnet"

    def get_data(self):
        response = requests.get(self.base_url)
        response.raise_for_status()
        data = response.json()
        return data