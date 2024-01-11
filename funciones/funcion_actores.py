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

def validar_actores():
    nombre_actor_a_validar = input("Ingrese nombre del actor: ")

    actor_encontrado = None

    for actor in lista_actores:
        if actor['nombre'].lower() == nombre_actor_a_validar.lower():
            actor_encontrado = actor
            break

    if actor_encontrado is not None:
        print(f"Actor encontrado:\n{actor_encontrado}")
        return actor_encontrado
    else:
        print("Actor no encontrado.")
        return None
