from utilidades.utilidades import *
from base_datos.funciones_datos import *
from funciones.funcion_generos import *
from funciones.funcion_actores import *
from funciones.funciones_formatos import *

def agregar_pelicula():
    limpiar_pantalla()
    id_pelicula = input("Ingrese ID de la película: ")
    nombre_pelicula = input("Ingrese nombre de la película: ")
    duracion_pelicula = input("Ingrese duración de la película: ")
    sinopsis_pelicula = input("Ingrese sinopsis de la película: ")
    
    genero_encontrado = validar_genero()
    
    if genero_encontrado:
        actor_encontrado = validar_actores()
        rol_actor = input("Ingrese rol del actor (Protagonista, Antagonista, Reparto): ")

        if actor_encontrado:
            formato_encontrado = validar_formatos()
            numero_copias = int(input("Ingrese número de copias: "))
            valor_prestamo = float(input("Ingrese valor de préstamo: "))

            pelicula = {
                id_pelicula: {
                    "id": id_pelicula,
                    "nombre": nombre_pelicula,
                    "duracion": duracion_pelicula,
                    "sinopsis": sinopsis_pelicula,
                    "generos": {
                        genero_encontrado["id"]: {
                            "id": genero_encontrado["id"],
                            "nombre": genero_encontrado["nombre"]
                        }
                    },
                    "actores": {
                        actor_encontrado['id']: {
                            "id": actor_encontrado['id'],
                            "nombre": actor_encontrado['nombre'],
                            "rol": rol_actor
                        }
                    },
                    "formato": {
                        formato_encontrado['id']: {
                            "id": formato_encontrado['id'],
                            "nombre": formato_encontrado['nombre'],
                            "NroCopias": numero_copias,
                            "valorPrestamo": valor_prestamo
                        }
                    }
                }
            }

            lista_peliculas.append(pelicula)
            print("Se creó la película con éxito")
            guardar_peliculas_json()
            return pelicula
        else:
            print("Actor no encontrado. La película no se creó.")
            return None
    else:
        print("Género no encontrado. La película no se creó.")
        return None

def modificar_pelicula():
    limpiar_pantalla()
    nombre_pelicula_a_modificar = input("Ingrese el nombre de la película que desea modificar: ")

    pelicula_encontrada = None

    for pelicula in lista_peliculas:
        if pelicula[list(pelicula.keys())[0]]["nombre"].lower() == nombre_pelicula_a_modificar.lower():
            pelicula_encontrada = pelicula
            break

    if pelicula_encontrada is not None:
        print("Detalles actuales de la película:")
        print(pelicula_encontrada)

        nuevo_id = input("Ingrese el nuevo ID de la película (deje en blanco para mantener el actual): ")
        nuevo_nombre = input("Ingrese el nuevo nombre de la película (deje en blanco para mantener el actual): ")
        nueva_duracion = input("Ingrese la nueva duración de la película (deje en blanco para mantener la actual): ")
        nueva_sinopsis = input("Ingrese la nueva sinopsis de la película (deje en blanco para mantener la actual): ")

        if nuevo_id:
            pelicula_encontrada[list(pelicula_encontrada.keys())[0]]["id"] = nuevo_id
        if nuevo_nombre:
            pelicula_encontrada[list(pelicula_encontrada.keys())[0]]["nombre"] = nuevo_nombre
        if nueva_duracion:
            pelicula_encontrada[list(pelicula_encontrada.keys())[0]]["duracion"] = nueva_duracion
        if nueva_sinopsis:
            pelicula_encontrada[list(pelicula_encontrada.keys())[0]]["sinopsis"] = nueva_sinopsis

        print("Detalles actualizados de la película:")
        print(pelicula_encontrada)

        guardar_peliculas_json()

        print("Película modificada con éxito.")
    else:
        print("Película no encontrada. No se realizaron modificaciones.")
        
        
def eliminar_pelicula():
    limpiar_pantalla()
    nombre_pelicula_a_eliminar = input("Ingrese el nombre de la película que desea eliminar: ")

    pelicula_encontrada = None

    for pelicula in lista_peliculas:
        if pelicula[list(pelicula.keys())[0]]["nombre"].lower() == nombre_pelicula_a_eliminar.lower():
            pelicula_encontrada = pelicula
            break

    if pelicula_encontrada is not None:
        print("Detalles de la película a eliminar:")
        print(pelicula_encontrada)

        confirmacion = input("¿Está seguro de que desea eliminar esta película? (s/n): ").lower()

        if confirmacion == 's':
            lista_peliculas.remove(pelicula_encontrada)
            guardar_peliculas_json()
            print("Película eliminada con éxito.")
        else:
            print("Operación cancelada. La película no se eliminó.")
    else:
        print("Película no encontrada. No se realizaron eliminaciones.")
        
def eliminar_actor():
    limpiar_pantalla()
    print("Lista de Actores:")
    listar_actores()

    nombre_actor_a_eliminar = input("Ingrese el nombre del actor que desea eliminar: ")

    actor_encontrado = None

    for actor in lista_actores:
        if actor["nombre"].lower() == nombre_actor_a_eliminar.lower():
            actor_encontrado = actor
            break

    if actor_encontrado is not None:
        print("Detalles del actor a eliminar:")
        print(actor_encontrado)

        confirmacion = input("¿Está seguro de que desea eliminar este actor? (s/n): ").lower()

        if confirmacion == 's':
            lista_actores.remove(actor_encontrado)
            guardar_actores_json()
            print("Actor eliminado con éxito.")
        else:
            print("Operación cancelada. El actor no se eliminó.")
    else:
        print("Actor no encontrado. No se realizaron eliminaciones.")

def buscar_pelicula_por_nombre():
    limpiar_pantalla()
    nombre_pelicula_a_buscar = input("Ingrese el nombre de la película que desea buscar: ")

    pelicula_encontrada = None

    for pelicula in lista_peliculas:
        if pelicula[list(pelicula.keys())[0]]["nombre"].lower() == nombre_pelicula_a_buscar.lower():
            pelicula_encontrada = pelicula
            break

    if pelicula_encontrada is not None:
        print("Película encontrada:")
        print(pelicula_encontrada)
    else:
        print("Película no encontrada.")

def listar_todas_las_peliculas():
    limpiar_pantalla()
    print("Listado de Todas las Películas:")
    for pelicula in lista_peliculas:
        print(pelicula)
        print("------------------------")
