if __name__ == "__main__":

    import numpy as np
    import scrap
    import fecha
    import prediction
    
    

    
    # Crear una instancia de la clase Matrix para el Rayo Vallecano
    rayo = scrap.Matrix('Rayo-Vallecano')

    # Crear una instancia de la clase Matrix para el Barcelona
    barcelona = scrap.Matrix('Barcelona')

    # Obtener los datos de estadísticas del equipo Rayo Vallecano
    rayo_stats = rayo.get_equipo()
    print(rayo_stats)

    # Obtener los datos de estadísticas del equipo Barcelona
    barcelona_stats = barcelona.get_equipo()
    print(barcelona_stats)