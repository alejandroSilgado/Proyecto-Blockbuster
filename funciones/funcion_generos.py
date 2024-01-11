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
    print("Listado de generos: ")
    for genero in lista_generos:
        print(f"ID : {genero['id']} ")
        print(f"Nombre del Genero: {genero['nombre']}")
        print("------------------------")

def validar_genero():
    nombre_genero_a_validar = input("Ingrese el nombre del género: ")

    genero_encontrado = None

    for genero in lista_generos:
        if genero['nombre'].lower() == nombre_genero_a_validar.lower():
            genero_encontrado = genero
            break

    if genero_encontrado is not None:
        print(f"Género encontrado:\n{genero_encontrado}")
        return genero_encontrado
    else:
        print("Género no encontrado.")
        return None
