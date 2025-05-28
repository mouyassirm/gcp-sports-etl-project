import requests

url = "https://v3.football.api-sports.io/fixtures"
headers = {
    "x-apisports-key": "f93ccd56bdfbf71298755f2a0ef8baab"
}
params = {
    "league": 61,        # ID Ligue 1
    "season": 2023       # Saison actuelle
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    for match in data['response'][:5]:  # Affiche les 5 premiers
        print(f"{match['teams']['home']['name']} vs {match['teams']['away']['name']} - {match['fixture']['date']}")
else:
    print("Erreur:", response.status_code, response.text)


