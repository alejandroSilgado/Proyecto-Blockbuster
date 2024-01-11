import json
import os

# GENEROS.JSON 

def cargar_generos_json():
    try:
        with open(os.path.join("base_datos", "generos.json"), 'r') as archivo_json:
            lista_generos = json.load(archivo_json)
        print("La lista de generos ha sido cargada")
        return lista_generos
    except FileNotFoundError:
        return []

def guardar_generos_json():
    try:
        with open(os.path.join("base_datos", "generos.json"), 'w') as archivo_json: 
            json.dump(lista_generos, archivo_json, indent=2)
        print("La lista de generos ha sido guardada")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        
lista_generos = cargar_generos_json()
# ACTORES.JSON 
def cargar_actores_json():
    try:
        with open(os.path.join("base_datos", "actores.json"), 'r') as archivo_json:
            lista_actores = json.load(archivo_json)
        print("La lista de actores ha sido cargada")
        return lista_actores
    except FileNotFoundError:
        return []

def guardar_actores_json():
    try:
        with open(os.path.join("base_datos", "actores.json"), 'w') as archivo_json: 
            json.dump(lista_actores, archivo_json, indent=2)
        print("La lista de actores ha sido guardada")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        
lista_actores = cargar_actores_json()

# FORMATOS.JSON

def cargar_formatos_json():
    try:
        with open(os.path.join("base_datos", "formatos.json"), 'r') as archivo_json:
            lista_formatos = json.load(archivo_json)
        print("La lista de formatos ha sido cargada")
        return lista_formatos
    except FileNotFoundError:
        return []

def guardar_formatos_json():
    try:
        with open(os.path.join("base_datos", "formatos.json"), 'w') as archivo_json: 
            json.dump(lista_formatos, archivo_json, indent=2)
        print("La lista de formatos ha sido guardada")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        
lista_formatos = cargar_formatos_json()

# INFROMES.JSON
def cargar_informes_json():
    try:
        with open(os.path.join("base_datos", "informes.json"), 'r') as archivo_json:
            lista_informes = json.load(archivo_json)
        print("La lista de informes ha sido cargada")
        return lista_informes
    except FileNotFoundError:
        return []

def guardar_informes_json():
    try:
        with open(os.path.join("base_datos", "informes.json"), 'w') as archivo_json: 
            json.dump(lista_informes, archivo_json, indent=2)
        print("La lista de informes ha sido guardada")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        
lista_informes = cargar_informes_json()

# PELICULAS.JSON 

def cargar_peliculas_json():
    try:
        with open(os.path.join("base_datos", "peliculas.json"), 'r') as archivo_json:
            lista_peliculas = json.load(archivo_json)
        print("La lista de peliculas ha sido cargada")
        return lista_peliculas
    except FileNotFoundError:
        return []

def guardar_peliculas_json():
    try:
        with open(os.path.join("base_datos", "peliculas.json"), 'w') as archivo_json: 
            json.dump(lista_peliculas, archivo_json, indent=2)
        print("La lista de peliculas ha sido guardada")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        
lista_peliculas = cargar_peliculas_json()
