from base_datos.funciones_datos import *
from utilidades.utilidades import *

def crear_formato():
    id_formato = input("Ingrese ID del formato: ")
    nombre_formato = input("Ingrese nombre del formato: ")

    formato = {
        "id": id_formato,
        "nombre": nombre_formato
    }
    lista_formatos.append(formato)
    print("Se creó el formato con éxito")
    guardar_formatos_json()
    return formato

def listar_formatos():
    limpiar_pantalla()
    print("Listado de formatos: ")
    for formato in lista_formatos:
        print(f"ID : {formato['id']} ")
        print(f"Nombre del Formato: {formato['nombre']}")
        print("------------------------")