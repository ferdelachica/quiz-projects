import requests

url = "https://balldontlie.io/api/v1/players"

response = requests.get(url)

data = response.json()["data"]

for players in data:
    player_name = players["last_name"]
    team_name = players["team"]["name"]
    print(f'{player_name} - {team_name}')
