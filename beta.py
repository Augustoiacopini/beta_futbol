
from tkinter import ttk
from fecha import Fecha
import xgboost as xgb
import prediction
import tkinter
import pickle
import scrap


# Cargar modelo
xgboost = "modelo_xgboost.pkl"
with open(xgboost, 'rb') as archivo:
    modelo = pickle.load(archivo)


class_mapping = {'Alaves': 0,
                'Almeria': 1,
                'Athletic Club': 2,
                'Atletico Madrid': 3,
                'Barcelona': 4,
                'Betis': 5,
                'Celta Vigo': 6,
                'Cadiz': 7,
                'Eibar': 8,
                'Elche': 9,
                'Espanyol': 10,
                'Getafe': 11,
                'Girona': 12,
                'Granada': 13,
                'Huesca': 14,
                'La Coruña': 15,
                'Las Palmas': 16,
                'Leganes': 17,
                'Levante': 18,
                'Mallorca': 19,
                'Malaga': 20,
                'Osasuna': 21,
                'Rayo Vallecano': 22,
                'Real Madrid': 23,
                'Real Sociedad': 24,
                'Sevilla': 25,
                'Valencia': 26,
                'Valladolid': 27,
                'Villarreal': 28}



ventana = tkinter.Tk()

ventana.geometry("750x900")
etiqueta = tkinter.Label(ventana, text=">>>Liga española Prediccion<<<", bg = "green")
etiqueta.pack(fill = tkinter.X)


# Separador horizontal
sep_horizontal = ttk.Separator(ventana, orient="horizontal")
sep_horizontal.pack(fill="x", padx=10, pady=130)

entrada = tkinter.Entry(ventana)
entrada.place(x=200 ,y=100)

entrada2 = tkinter.Entry(ventana)
entrada2.place(x=400 ,y=100)

texto = tkinter.Label(ventana, text="Fecha", bg= "white")
texto.place(x= 300, y=100)

texto0 = tkinter.Label(ventana, text="Semana", bg= "white")
texto0.place(x= 500, y=100)

texto1 = tkinter.Label(ventana, text="Local", bg= "white", bd=2, highlightbackground="green")
texto1.place(x=50, y=250)

texto2 = tkinter.Label(ventana, text="Visitante", bg = "white", bd= 2, highlightbackground="green")
texto2.place(x=200, y=250)

text2 = tkinter.Label(ventana, text="Equipos", bg = "white", bd= 2, highlightbackground="green")
text2.place(x=100, y=180)

texto3 = tkinter.Label(ventana, text="Predicciones (%)", bg = "white", bd= 4, highlightbackground="green")
texto3.place(x=400, y=180)

texto4 = tkinter.Label(ventana, text="Victoria Local", bg = "white", bd= 2, highlightbackground="green")
texto4.place(x=300, y=250)

texto5 = tkinter.Label(ventana, text="Empate", bg = "white", bd= 2, highlightbackground="green")
texto5.place(x=450, y=250)

texto6 = tkinter.Label(ventana, text="Victoria Visitante", bg = "white", bd= 2, highlightbackground="green")
texto6.place(x=550, y=250)



def fecha():
	txt_fecha = entrada.get()
	#print(str(txt_fecha))   #entrada fecha 
	mi_fecha = Fecha(txt_fecha)
	enfrentamientos = mi_fecha.obtener_enfrentamientos()
	c = len(enfrentamientos)
	f = 250

	for p in range(c):

		f = f + 40
		local = tkinter.Label(ventana, text=f"{enfrentamientos[p].get('equipo_local')}")
		local.place(x=50, y=f)


		visitante = tkinter.Label(ventana, text=f"{enfrentamientos[p].get('equipo_visitante')}")
		visitante.place(x=200, y=f)

		id_enfrentamiento = enfrentamientos[p].get('id_enfrentamiento')

		bp = prediction.beta_p(id_enfrentamiento)

		resultado = bp.result()

		porcentaje = resultado[0].get("percent")



		home = str(porcentaje.get('home'))
		home = home.replace('%', '')
		home_a = float(home)

		draw = porcentaje.get('draw')
		draw = draw.replace('%', '')
		draw_a = float(draw)

		away = porcentaje.get('away')
		away = away.replace('%', '')
		away_a = int(away)


		n_local = enfrentamientos[p].get('equipo_local')
		n_visitante = enfrentamientos[p].get('equipo_visitante')
  		

		
		n_local = n_local.replace(' ', '-')

		n_visitante = n_visitante.replace(' ', '-')


		vector_local = scrap.Matrix(n_local)
		vector_visitante = scrap.Matrix(n_visitante)

		#matriz para predecir resultado
		vector_local = vector_local.hack()
		vector_visitante = vector_visitante.hack()

		#'Sem.', 'Local', 'Visitante', importante antes de unir las listas


		vector_fecha = list([float(entrada2.get()), float(class_mapping.get(enfrentamientos[p].get('equipo_local'))), float(class_mapping.get(enfrentamientos[p].get('equipo_visitante')))])
		vector_fecha.extend(vector_visitante)
		vector_fecha.extend(vector_local)
		vector = vector_fecha

		model_est_xgboost = modelo.predict_proba([vector])*100
		est_xgboost = model_est_xgboost[0]


		home_xg = est_xgboost[1]
		draw_xg = est_xgboost[0]
		away_xg = est_xgboost[2]

		# Calcular el porcentaje general para cada valor del diccionario
		home_general = home_a * home_xg / 100 / sum(est_xgboost) * 100
		draw_general = draw_a * draw_xg / 100 / sum(est_xgboost) * 100
		away_general = away_a * away_xg / 100 / sum(est_xgboost) * 100

		# Redondear los resultados a dos decimales
		home_general = round(home_general, 2)
		draw_general = round(draw_general, 2)
		away_general = round(away_general, 2)

		total_general = home_general + draw_general + away_general
		ajuste = 100 - total_general
		away_general += ajuste


		porc_h = tkinter.Label(ventana, text=f"{away_general}")
		porc_h.place(x=300, y=f)

		porc_d = tkinter.Label(ventana, text=f"{draw_general}")
		porc_d.place(x=450, y=f)

		porc_a = tkinter.Label(ventana, text=f"{home_general}")
		porc_a.place(x=550, y=f)




		
prediccion = tkinter.Button(ventana, text="prediccion", command= fecha)
prediccion.place(x=100, y=100)





ventana.mainloop()