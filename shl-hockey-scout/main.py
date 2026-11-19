import requests
from shl_api import SHLApi
from hockey_scout import SHLhockeyscout

shl_api = SHLApi()
data = shl_api.get_data()

hockey_scout = SHLhockeyscout(data)
players = hockey_scout.find_player()
print(players["TOI_GP"])

