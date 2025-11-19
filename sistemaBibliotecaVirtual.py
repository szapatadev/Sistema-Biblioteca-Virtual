import json

archivo = "biblioteca.json"

def verLibrosDisponible ():
    print("Ver libros disponibles")

def agregarNuevosLibro ():
    print("Agregar nuevos libros")

def prestarLibros():
    print("Prestar libros")

def devolverLibros():
    print("Devolver libros")

def historial():
    print("Historial")

programa = 0

while programa != 6:
    try:
        print("1 - Ver libros disponibles\n" \
        "2 - Agregar nuevos libros\n" \
        "3 - Prestar libro\n" \
        "4 - Devolver libros\n" \
        "5 - Devolver libros\n" \
        "6 - Salir")
        programa = int(input("Que quieres hacer? "))
    except:
        print("Ingresa un valor valido\n")
    
    if programa < 1 or programa > 6:
        print("Ingresa un valor valido\n")

    if programa == 1:
        verLibrosDisponible()

    if programa == 2:
        agregarNuevosLibro()

    if programa == 3:
        prestarLibros()

    if programa == 4:
        devolverLibros()

    if programa == 5:
        historial()