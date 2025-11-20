import json

archivo = "biblioteca.json"

def cargarDatos():
    try:
        with open (archivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        guardarDatos([])
        return []
    except json.JSONDecodeError:
        print ("Se creará un nuevo archivo\n")
        guardarDatos
        return []
   
def guardarDatos(data):
    with open (archivo, "w") as f:
     json.dump (data, f, indent = (4))

def verLibrosDisponible (lista):
    if not lista:
        print ("No hay libros registrados\n")
    else:
        print ("--- Lista de libros ---")
        for i in lista:
            print (f"Nombre: {i["nombre"]} | Estado: {i["estado"]}")
    print("")

def agregarNuevosLibro (lista):
    nombre = input("Nombre del libro: ") 
    estado = input("Ingresa el estado (Prestado o Inventario): ")
    
    libro = {"nombre" : nombre, "estado" : estado}

    lista.append(libro)
    guardarDatos(lista)
    print("Libro agregado correctamente.\n")

def prestarLibros(lista):
    verLibrosDisponible(lista)
    nombreBuscar = input("Nombre del libro a prestar: ")

    for i in lista:
        if i["nombre"] == nombreBuscar:
            if i["estado"] != "Prestado":
                i["estado"] = "Prestado"
                guardarDatos(lista) 
                print("Perfecto, recuerda devolverlo.")
                return
            else:
                print("El libro ya esta prestado\n")
                return
    print("No se encontró el libro.\n")

def devolverLibros(lista):
    verLibrosDisponible(lista)
    nombreBuscar = input("Nombre del libro a devolver: ")

    for i in lista:
        if i["nombre"] == nombreBuscar:
            if i["estado"] == "Prestado":
                i["estado"] = "Inventario"
                guardarDatos(lista) 
                print("Perfecto, ya se devolvio.\n")
                return
            else:
                print("El libro esta en inventario\n")
                return
    print("No se encontró el libro.\n")

programa = 0

while programa != 5:
    try:
        print("1 - Ver libros disponibles\n" \
        "2 - Agregar nuevos libros\n" \
        "3 - Prestar libro\n" \
        "4 - Devolver libros\n" \
        "5 - Salir")
        programa = int(input("Que quieres hacer? "))
    except:
        print("Ingresa un valor valido\n")

    print("")
    
    if programa < 1 or programa > 6:
        print("Ingresa un valor valido\n")
    
    lista = cargarDatos()

    if programa == 1:
        verLibrosDisponible(lista)

    if programa == 2:
        agregarNuevosLibro(lista)

    if programa == 3:
        prestarLibros(lista)

    if programa == 4:
        devolverLibros(lista)