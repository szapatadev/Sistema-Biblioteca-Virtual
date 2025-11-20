import json # Importamos JSON para guardar y cargar la base de datos de libros

# Nombre del archivo donde se almacenarán los datos
archivo = "biblioteca.json"

def cargarDatos():
    """
    Carga los datos desde el archivo JSON.
    Si no existe, crea uno nuevo.
    Si está dañado, también crea uno nuevo.
    """
    try:
        # Intentar abrir el archivo en modo lectura
        with open (archivo, "r") as f:
            return json.load(f) # Convertir JSON a lista/diccionario
    except FileNotFoundError:
        # Si el archivo no existe, lo creamos vacío
        guardarDatos([])
        return []
    except json.JSONDecodeError:
        # Si el archivo está corrupto o vacío
        print ("Se creará un nuevo archivo\n")
        guardarDatos([])
        return []
   
def guardarDatos(data):
    """
    Guarda en el archivo JSON la lista completa de libros.
    """
    with open (archivo, "w") as f:
     json.dump (data, f, indent = (4)) # indent=4 para que quede bonito

def verLibrosDisponible (lista):
    """
    Muestra los libros registrados en el sistema.
    """
    if not lista:
        print ("No hay libros registrados\n")
    else:
        print ("--- Lista de libros ---")
        for i in lista:
            # Mostrar información de cada libro
            print (f"Nombre: {i["nombre"]} | Estado: {i["estado"]}")
    print("") # Espacio por estética

def agregarNuevosLibro (lista):
    """
    Agrega un libro al inventario.
    """
    nombre = input("Nombre del libro: ") 
    estado = input("Ingresa el estado (Prestado o Inventario): ")

    # Crear un diccionario para guardar el libro
    libro = {"nombre" : nombre, "estado" : estado}

    lista.append(libro) # Agregar a la lista
    guardarDatos(lista) # Guardar en JSON
    print("Libro agregado correctamente.\n")

def prestarLibros(lista):
    """
    Cambia el estado de un libro a 'Prestado' si está disponible.
    """
    verLibrosDisponible(lista)
    nombreBuscar = input("Nombre del libro a prestar: ")

    for i in lista:
        if i["nombre"] == nombreBuscar:
            if i["estado"] != "Prestado":
                # Cambiamos su estado a prestado
                i["estado"] = "Prestado"
                guardarDatos(lista) 
                print("Perfecto, recuerda devolverlo.")
                return
            else:
                print("El libro ya esta prestado\n")
                return
    # Si sale del ciclo sin return, no se encontró
    print("No se encontró el libro.\n")

def devolverLibros(lista):
    """
    Cambia el estado de un libro de 'Prestado' a 'Inventario'.
    """
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

# Variable para controlar la ejecución del programa
programa = 0


# Bucle principal del menú
while programa != 5:
    try:
        # Menú para el usuario
        print("1 - Ver libros disponibles\n" \
        "2 - Agregar nuevos libros\n" \
        "3 - Prestar libro\n" \
        "4 - Devolver libros\n" \
        "5 - Salir")
        programa = int(input("Que quieres hacer? "))
    except:
        print("Ingresa un valor valido\n")

    print("")
    
    # Validación del rango
    if programa < 1 or programa > 5:
        print("Ingresa un valor valido\n")

    # Cargar la base de datos antes de ejecutar una opción
    lista = cargarDatos()

    # Ejecutar cada opción según lo que el usuario escoge
    if programa == 1:
        verLibrosDisponible(lista)

    if programa == 2:
        agregarNuevosLibro(lista)

    if programa == 3:
        prestarLibros(lista)

    if programa == 4:
        devolverLibros(lista)