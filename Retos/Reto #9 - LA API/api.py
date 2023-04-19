import requests

url = "https://balldontlie.io/api/v1/players"

response = requests.get(url)


for players in response.json()["data"]:
    consulta = [players["last_name"], players["name"]]
    print(consulta)