import pandas as pd

#Clase que devuelve 

class Matrix:
 

    
        
    def __init__(self, club):
        """>>matriz_local = scrap.matrix('Rayo-Vallecano')
            >>[vector] """
        self.club = club
        self.equipo = []
        
    import pandas as pd 

        
    def hack(self):
        
        class_mapping = {'Alaves': 'https://fbref.com/es/equipos/8d6fd021/Alaves-Stats',
                'Almeria': 'https://fbref.com/es/equipos/78ecf4bb/Estadisticas-de-Almeria',
                'Athletic-Club': 'https://fbref.com/es/equipos/2b390eca/Estadisticas-de-Athletic-Club',
                'Atletico-Madrid': 'https://fbref.com/es/equipos/db3b9613/Estadisticas-de-Atletico-Madrid',
                'Barcelona': 'https://fbref.com/es/equipos/206d90db/Estadisticas-de-Barcelona',
                'Betis': 'https://fbref.com/es/equipos/fc536746/Estadisticas-de-Real-Betis',
                'Celta-Vigo': 'https://fbref.com/es/equipos/f25da7fb/Estadisticas-de-Celta-Vigo',
                'Cadiz': 'https://fbref.com/es/equipos/ee7c297c/Estadisticas-de-Cadiz',
                'Eibar': 'https://fbref.com/es/equipos/bea5c710/Estadisticas-de-Eibar',
                'Elche': 'https://fbref.com/es/equipos/6c8b07df/Estadisticas-de-Elche',
                'Espanyol': 'https://fbref.com/es/equipos/a8661628/Estadisticas-de-Espanyol',
                'Getafe': 'https://fbref.com/es/equipos/7848bd64/Estadisticas-de-Getafe',
                'Girona': 'https://fbref.com/es/equipos/9024a00a/Estadisticas-de-Girona',
                'Granada': 'https://fbref.com/es/equipos/a0435291/Granada-Stats',
                'Huesca': 'https://fbref.com/es/equipos/c6c493e6/Huesca-Stats',
                'La-Coruña': 'https://fbref.com/es/equipos/2a60ed82/Deportivo-La-Coruna-Stats',
                'Las-Palmas': 'https://fbref.com/es/equipos/0049d422/Las-Palmas-Stats',
                'Leganes': 'https://fbref.com/es/equipos/7c6f2c78/Leganes-Stats',
                'Levante': 'https://fbref.com/es/equipos/9800b6a1/Levante-Stats',
                'Mallorca': 'https://fbref.com/es/equipos/2aa12281/Estadisticas-de-Mallorca',
                'Malaga': 'https://fbref.com/es/equipos/1c896955/Malaga-Stats',
                'Osasuna': 'https://fbref.com/es/equipos/03c57e2b/Estadisticas-de-Osasuna',
                'Rayo-Vallecano': 'https://fbref.com/es/equipos/98e8af82/Estadisticas-de-Rayo-Vallecano',
                'Real-Madrid': 'https://fbref.com/es/equipos/53a2f082/Estadisticas-de-Real-Madrid',
                'Real-Sociedad': 'https://fbref.com/es/equipos/e31d1cd9/Estadisticas-de-Real-Sociedad',
                'Sevilla': 'https://fbref.com/es/equipos/ad2be733/Estadisticas-de-Sevilla',
                'Valencia': 'https://fbref.com/es/equipos/dcc91a7b/Estadisticas-de-Valencia',
                'Valladolid': 'https://fbref.com/es/equipos/17859612/Estadisticas-de-Valladolid',
                'Villarreal': 'https://fbref.com/es/equipos/2a8183b3/Estadisticas-de-Villarreal'}
        
        def columna(columns):
            """funcion para renombrar columnas
            >>columna(pd.columns)"""

            columna = list()

            for c in range(len(columns)):
                columna.append(columns[c][1])
            return columna
        
        data = pd.read_html(class_mapping.get(self.club))

        resumen = data[0]
        resumen.columns = columna(resumen.columns)
        resumen = (resumen[['Ass', 'xG', 'xAG']].fillna(0.0))
        resumen = resumen.loc[:, ~resumen.columns.duplicated()]


        pases = data[5]
        pases.columns = columna(pases.columns)
        pases = pases[['% Cmp', 'xA']].fillna(0.0)
        pases = pases.loc[:, ~pases.columns.duplicated()]


        t_pases = data[6]
        t_pases.columns = columna(t_pases.columns)
        t_pases = t_pases[['Pcz', 'Balón muerto']].fillna(0.)

        acci_d = data[8]
        acci_d.columns = columna(acci_d.columns)
        acci_d = acci_d[['Desp.']]


        pos_b = data[9]
        pos_b.columns = columna(pos_b.columns)
        pos_b = pos_b[['Def. pen.', 'Ataq. pen.', 'TAP', ]]


        equipo = pd.concat([resumen, pases, t_pases, acci_d, pos_b], axis=1)
        equipo.fillna(0.)
        equipo = equipo[['Ass', 'xG', 'Pcz', 'Desp.', 'xAG', 'TAP', 'Def. pen.', 'Balón muerto', 'xA', '% Cmp', 'Ataq. pen.']]
        equipo = (equipo.iloc[:-2].mean())
        
        
        self.equipo = list(equipo.values)
        return  self.equipo


#fin de la clase

