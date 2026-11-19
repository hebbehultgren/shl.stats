import requests
from shl_api import SHLApi
from hockey_scout import SHLhockeyscout

shl_api = SHLApi()
data = shl_api.get_data()

hockey_scout = SHLhockeyscout(data)
players = hockey_scout.get_players()
print(len(players))
