from base_datos.funciones_datos import *
from utilidades.utilidades import *

def crear_actor():
    id_actor = input("Ingrese ID del actor: ")
    nombre_actor = input("Ingrese nombre del actor: ")

    actor = {
        "id": id_actor,
        "nombre": nombre_actor
    }
    lista_actores.append(actor)
    print("Se creó el actor con éxito")
    guardar_actores_json()
    return actor

def listar_actores():
    limpiar_pantalla()
    print("Listado de actores: ")
    for actor in lista_actores:
        print(f"ID : {actor['id']} ")
        print(f"Nombre del Actor: {actor['nombre']}")
        print("------------------------")
