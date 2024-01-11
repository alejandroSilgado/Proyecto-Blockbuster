from base_datos.funciones_datos import *
from utilidades.utilidades import *

def crear_genero():
    id_genero = input("Ingrese id genero: ")
    nombre_genero = input("Ingrese nombre genero: ")

    genero = {
        "id": id_genero,
        "nombre": nombre_genero
    }
    lista_generos.append(genero)
    print("Se creó el genero con éxito")
    guardar_generos_json()
    return genero

def listar_generos():
    limpiar_pantalla()
    print("Listado de campers: ")
    for genero in lista_generos:
        print(genero)

