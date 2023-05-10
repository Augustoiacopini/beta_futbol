import requests

class beta_p:

    def __init__(self, id):
        """
        devuelve prediccion del partido segun 
        la
        distribución de Poisson
        """

        self.id = id
        self.lista = []

        url = "https://api-football-beta.p.rapidapi.com/predictions?"

        querystring = {"fixture":self.id}

        headers = {"x-rapidapi-key": "*******************************",
                    "x-rapidapi-host": "api-football-beta.p.rapidapi.com"}
        response = requests.request("GET", url, headers=headers, params=querystring)

        data = response.json()

        dicc =  data.get('response')[0].get('predictions')
        self.lista = [dicc]
    
    def result(self):
        
        return self.lista
    
    
