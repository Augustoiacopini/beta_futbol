import requests

class Fecha:
    def __init__(self, fecha):
        """formato '2023-04-29'"""
        self.fecha = fecha
        self.enfrentamientos = []
        
        url = "https://api-football-beta.p.rapidapi.com/fixtures"
            
        querystring = {"league":"140","season":2022,"date":self.fecha}

        headers = {"x-rapidapi-key": "2ede2642bbmshcf1ffab0810726cp198229jsn6890c02ecc02",
                    "x-rapidapi-host": "api-football-beta.p.rapidapi.com"}

        response = requests.request("GET", url, headers=headers, params=querystring)

        data = response.json()

        for partido in data.get('response'):
            id_enfrentamiento = partido.get('fixture').get('id')
            equipo_local = partido.get('teams').get('home').get('name')
            equipo_visitante =  partido.get('teams').get('away').get('name')
            id_local = partido.get('teams').get('home').get('id')        
            id_visitante = partido.get('teams').get('away').get('id')
            enfrentamiento = {'id_enfrentamiento': id_enfrentamiento, 
                              'equipo_local': equipo_local, 
                              'equipo_visitante': equipo_visitante,
                              'id_local': id_local,
                              'id_visitante': id_visitante}
            self.enfrentamientos.append(enfrentamiento)
            
    def obtener_enfrentamientos(self):
        return self.enfrentamientos

       
        
        

#fin de clase