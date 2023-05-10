import requests
""" devuelve todos los equipos de la liga española"""
url = f"https://api-football-beta.p.rapidapi.com/teams?"
headers = {"x-rapidapi-key": "*********************************",
                    "x-rapidapi-host": "api-football-beta.p.rapidapi.com"}

querystring = {"league":140, "season":2022}
response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()



#print(data)
