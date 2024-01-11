from utilidades.utilidades import *
from commons.menus import *
from funciones.funcion_generos import *
from funciones.funcion_actores import *
from funciones.funciones_formatos import *
from funciones.funcion_peliculas import *
from funciones.funcion_informes import *
#Arranque del menu generos
#FUNCIONAL

def generos():
    limpiar_pantalla()
    op = menu_generos()
    if op==1:
        crear_genero()
        input("Clic cualquier teclas [continuar]: ")
    if op==2:
        listar_generos()
        input("Clic cualquier teclas [continuar]: ")

#Arranque del menu Actores
#FUNCIONAL
      
def actores():
    limpiar_pantalla()
    op = menu_actores()
    if op==1:
        crear_actor()
        input("Clic cualquier teclas [continuar]: ")
    if op==2:
        listar_actores()
        input("Clic cualquier teclas [continuar]: ")

#Arranque del menu Fromatos
#FUNCIONAL

def formatos():
    limpiar_pantalla()
    op = menu_formatos()
    if op==1:
        crear_formato()
        input("Clic cualquier teclas [continuar]: ")
    if op==2:
        listar_formatos()
        input("Clic cualquier teclas [continuar]: ")

def informes():
    limpiar_pantalla()
    op = menu_informes()
    if op == 1:
        listar_peliculas_por_nombre_genero()
        input("Clic cualquier teclas [continuar]: ")
    if op == 2:
        listar_peliculas_por_nombre_actor()
        input("Clic cualquier teclas [continuar]: ")
    if op == 3:
        buscar_pelicula_por_nombre()
        input("Clic cualquier teclas [continuar]: ")
        
        
def peliculas():
    limpiar_pantalla()
    op = menu_peliculas()
    if op == 1:
        agregar_pelicula()
        input("Clic cualquier teclas [continuar]: ")
    if op == 2:
        modificar_pelicula()
        input("Clic cualquier teclas [continuar]: ")
    if op == 3:
        eliminar_pelicula()
        input("Clic cualquier teclas [continuar]: ")
    if op == 4:
        eliminar_actor()
        input("Clic cualquier teclas [continuar]: ")
    if op == 5:
        buscar_pelicula_por_nombre()
        input("Clic cualquier teclas [continuar]: ")
    if op == 6:
        listar_todas_las_peliculas()
        input("Clic cualquier teclas [continuar]: ")
        
# Arranque del menú principal
while True:
    limpiar_pantalla()
    op = menu_principal()
    if op == 1:
        generos()
    elif op == 2:
        actores()
    elif op == 3:
        formatos()
    elif op == 4:
        informes()
    elif op == 5:
        peliculas()
    elif op == 6:
        print("Saliendo")
        break
