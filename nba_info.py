import requests
from pprint import PrettyPrinter
from dotenv import load_dotenv, dotenv_values
import os


load_dotenv()

BASE_URL = "https://api.balldontlie.io"
API_KEY = os.getenv("MY_API_KEY")
HEADERS = {"Authorization": f"{API_KEY}"}

teams = "/v1/teams"
players = "/v1/players"


printer = PrettyPrinter()

player_response = requests.get(f"{BASE_URL}{players}", headers=HEADERS).json()
team_response = requests.get(f"{BASE_URL}{teams}", headers=HEADERS).json()

team_data = team_response
player_data = player_response['data']


def get_players_name():  

    players_fullname = []

    for info in player_data:
        entry = info['first_name'], info['last_name']
        players_fullname.append(entry)

    players_fullname = dict(players_fullname)
    return players_fullname


def get_player_and_team_info():

    player_and_team_info = []

    for info in player_data:
        entry = info['first_name'], info['team']
        player_and_team_info.append(entry)
    
    player_and_team_info = dict(player_and_team_info)
    
    return player_and_team_info


def team_and_abbreviation():
    team_abrv = []

    for info in player_data:
        entry = info['team']['full_name'], info['team']['abbreviation']
        team_abrv.append(entry)
    
    team_abrv = dict(team_abrv)

    return team_abrv



players = get_players_name()
player_and_team = get_player_and_team_info()
team_abbrev= team_and_abbreviation()

print("\n")
print("PLAYERS")
print("\n")
printer.pprint(players)
print("\n")
print("------------------------------------------------------")
print("\n")
print("TEAMS")
print("\n")
printer.pprint(team_data)
print("\n")
print("------------------------------------------------------")
print("\n")
print("PLAYER INFO")
print("\n")
printer.pprint(player_and_team)

