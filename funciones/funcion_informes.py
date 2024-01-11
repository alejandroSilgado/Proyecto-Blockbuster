from utilidades.utilidades import *
from base_datos.funciones_datos import *
from funciones.funcion_generos import *
from funciones.funcion_actores import *
from funciones.funciones_formatos import *

def listar_peliculas_por_nombre_genero():
    limpiar_pantalla()
    nombre_genero_a_buscar = input("Ingrese el nombre del género para listar películas: ")

    peliculas_del_genero = []

    for pelicula in lista_peliculas:
        generos_pelicula = pelicula[list(pelicula.keys())[0]]["generos"]

        for _, info_genero in generos_pelicula.items():
            if info_genero["nombre"].lower() == nombre_genero_a_buscar.lower():
                peliculas_del_genero.append(pelicula)
                break

    if peliculas_del_genero:
        print(f"Listado de Películas del Género '{nombre_genero_a_buscar}':")
        for pelicula in peliculas_del_genero:
            print(pelicula)
            print("------------------------")
    else:
        print(f"No se encontraron películas para el género '{nombre_genero_a_buscar}'.")

def listar_peliculas_por_nombre_actor():
    limpiar_pantalla()
    nombre_actor_a_buscar = input("Ingrese el nombre del actor para listar películas: ")

    peliculas_del_actor = []

    for pelicula in lista_peliculas:
        actores_pelicula = pelicula[list(pelicula.keys())[0]]["actores"]

        for _, info_actor in actores_pelicula.items():
            if info_actor["nombre"].lower() == nombre_actor_a_buscar.lower():
                peliculas_del_actor.append(pelicula)
                break

    if peliculas_del_actor:
        print(f"Listado de Películas con el Actor '{nombre_actor_a_buscar}':")
        for pelicula in peliculas_del_actor:
            print(pelicula)
            print("------------------------")
    else:
        print(f"No se encontraron películas con el actor '{nombre_actor_a_buscar}'.")

def buscar_pelicula_por_nombre():
    limpiar_pantalla()
    nombre_pelicula_a_buscar = input("Ingrese el nombre de la película para buscar: ")

    pelicula_encontrada = None

    for pelicula in lista_peliculas:
        if pelicula[list(pelicula.keys())[0]]["nombre"].lower() == nombre_pelicula_a_buscar.lower():
            pelicula_encontrada = pelicula
            break

    if pelicula_encontrada:
        limpiar_pantalla()
        print(f"Sinopsis de la película '{nombre_pelicula_a_buscar}':")
        print(pelicula_encontrada[list(pelicula_encontrada.keys())[0]]["sinopsis"])
        print("________________________________")
        print("\nActores:")
        actores_pelicula = pelicula_encontrada[list(pelicula_encontrada.keys())[0]]["actores"]
        for _, info_actor in actores_pelicula.items():
            print(f"Nombre del Actor: {info_actor['nombre']}, Rol: {info_actor['rol']}")

    else:
        print(f"No se encontró ninguna película con el nombre '{nombre_pelicula_a_buscar}'.")

