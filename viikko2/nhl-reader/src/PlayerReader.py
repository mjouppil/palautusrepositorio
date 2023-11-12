import requests
from player import Player


class PlayerReader:

    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        players = []
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        return players

# def player_reader():
#     url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
#     response = requests.get(url).json()
#
#     # print("JSON-muotoinen vastaus:")
#     # print(response)
#
#     players = []
#     for player_dict in response:
#         player = Player(player_dict)
#         players.append(player)
#
#     return players
