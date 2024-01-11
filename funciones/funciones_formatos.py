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
        
def validar_formatos():
    nombre_formato_a_validar = input("Ingrese nombre del formato: ")

    formato_encontrado = None

    for formato in lista_formatos:
        if formato['nombre'].lower() == nombre_formato_a_validar.lower():
            formato_encontrado = formato
            break

    if formato_encontrado is not None:
        print(f"Formato encontrado:\n{formato_encontrado}")
        return formato_encontrado
    else:
        print("Formato no encontrado.")
        return None