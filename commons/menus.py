from utilidades.utilidades import *


def menu_principal():
    limpiar_pantalla()
    print("----------Bienvenido al sistema de organizacion de BlockBuster---------------")
    print("1 Administrador de Generos")
    print("2 Administrador de Actores")
    print("3 Administrador de Formatos")
    print("4 Gestor de Informes")
    print("5 Gestor peliculas")
    print("6.Salir")
    op=verificar_opcion("Opcion: ",1,6)
    return op


def menu_generos():
    limpiar_pantalla()
    print("1. Crear genero")
    print("2.Listar generos")
    print("3 Ir Menu principal")
    op=verificar_opcion("Opcion: ",1,3)
    return op

def menu_actores():
    limpiar_pantalla()
    print("1. Crear actor")
    print("2. Listar actor")
    print("3. Ir Menu principal")
    op=verificar_opcion("Opcion: ",1,3)
    return op

def menu_formatos():
    limpiar_pantalla()
    print("1. Crear formatos")
    print("2. Listar formatos")
    print("3. Ir Menu principal")
    op=verificar_opcion("Opcion: ",1,3)
    return op


def menu_informes():
    limpiar_pantalla()
    print("1 Listar las peliculas de un genero especifico")
    print("2 Listar las peliculas de un actor especifico")
    print("3 Buscar pelicula y mostrar la sinopsis y los actores")
    print("4 Ir menu Principal")
    op=verificar_opcion("Opcion: ",1,4)
    return op

def menu_peliculas():
    limpiar_pantalla()
    print("1 Agregar pelicula")
    print("2 Editar pelicula")
    print("3 Eliminar pelicula")
    print("4 Eliminar Actor")
    print("5 Buscar pelicula")
    print("6 Listar todas peliculas")
    print("7 Menu principal")
    op=verificar_opcion("Opcion: ",1,7)
    return op
