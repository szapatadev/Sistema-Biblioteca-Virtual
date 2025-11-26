# Sistema de Biblioteca Virtual
Un sistema simple de gestión de libros hecho en Python, usando archivos JSON como base de datos.
Permite registrar libros, ver inventario, prestar y devolver ejemplares mediante un menú interactivo en consola.

## Características principales
- Ver libros disponibles
- Agregar nuevos libros
- Prestar un libro (cambia a “Prestado”)
- Devolver un libro (cambia a “Inventario”)
- Base de datos persistente en JSON
- Validaciones básicas y manejo de errores

## ¿Cómo funciona?
El programa utiliza un archivo: biblioteca.json
donde se almacenan todos los libros como una lista de diccionarios.
El sistema se encarga de:
- Crear el archivo si no existe
- Repararlo si está dañado o vacío
- Guardar cambios automáticamente

## Estructura del Código
- cargarDatos() Carga la base de datos desde biblioteca.json.
Crea uno nuevo si no existe o está corrupto.
- guardarDatos(lista) Guarda la lista completa de libros en formato JSON con indentación.
- verLibrosDisponible(lista) Muestra todos los libros registrados junto con su estado.
- agregarNuevosLibro(lista) Solicita al usuario: Nombre del libro, Estado (Prestado/Inventario), Luego lo guarda en la base de datos.
- prestarLibros(lista) Cambia un libro a estado Prestado, si está disponible.
- devolverLibros(lista) Cambia un libro a Inventario, si actualmente está prestado.
- Menú principal
