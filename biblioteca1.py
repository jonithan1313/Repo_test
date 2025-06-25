usuarios = [
    {"nombre": "Ana", "apellido": "González", "rut": "13816108-7", "libros": []},
    {"nombre": "Luis", "apellido": "Rodríguez", "rut": "13872719-2", "libros": []},
    {"nombre": "Camila", "apellido": "Pérez", "rut": "12182343-5", "libros": []},
    {"nombre": "Jorge", "apellido": "Muñoz", "rut": "14044461-9", "libros": []},
    {"nombre": "María", "apellido": "Rojas", "rut": "16149391-0", "libros": []},
    {"nombre": "Diego", "apellido": "Díaz", "rut": "10407062-4", "libros": []},
    {"nombre": "Lucía", "apellido": "Soto", "rut": "19306158-3", "libros": []},
    {"nombre": "Pablo", "apellido": "Torres", "rut": "14864522-5", "libros": []},
    {"nombre": "Valentina", "apellido": "Contreras", "rut": "15592214-1", "libros": []},
    {"nombre": "Tomás", "apellido": "Silva", "rut": "10516040-5", "libros": []}
]

# Listado inicial de libros
libros = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "ISBN": "978-0307474728", "paginas": 432, "cantidad_disponible": 5},
    {"id": 2, "titulo": "1984", "autor": "George Orwell", "ISBN": "978-0451524935", "paginas": 328, "cantidad_disponible": 3},
    {"id": 3, "titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "ISBN": "978-1451673319", "paginas": 194, "cantidad_disponible": 7},
    {"id": 4, "titulo": "Don Quijote", "autor": "Miguel de Cervantes", "ISBN": "978-0060934347", "paginas": 992, "cantidad_disponible": 2},
    {"id": 5, "titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "ISBN": "978-1400034956", "paginas": 128, "cantidad_disponible": 4},
    {"id": 6, "titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "ISBN": "978-0156013987", "paginas": 96, "cantidad_disponible": 10},
    {"id": 7, "titulo": "Ensayo sobre la ceguera", "autor": "José Saramago", "ISBN": "978-0156007757", "paginas": 352, "cantidad_disponible": 3},
    {"id": 8, "titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "ISBN": "978-0143034902", "paginas": 512, "cantidad_disponible": 6},
    {"id": 9, "titulo": "El túnel", "autor": "Ernesto Sabato", "ISBN": "978-9500402035", "paginas": 160, "cantidad_disponible": 2},
    {"id": 10, "titulo": "Pedro Páramo", "autor": "Juan Rulfo", "ISBN": "978-6073142360", "paginas": 144, "cantidad_disponible": 8}
]

# Función para buscar un usuario por RUT
def buscar_usuario(rut):
    for usuario in usuarios:
        if usuario["rut"] == rut:
            return usuario
    return None

# Función para registrar un nuevo usuario
def registrar_usuario():
    try:
        rut = input("Ingrese el RUT del nuevo usuario: ").strip()
        if buscar_usuario(rut):
            print("Este RUT ya está registrado.")
            return
        nombre = input("Ingrese el nombre: ").strip()
        apellido = input("Ingrese el apellido: ").strip()
        usuarios.append({"nombre": nombre, "apellido": apellido, "rut": rut, "libros": []})
        print(f"Usuario {nombre} {apellido} registrado exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al registrar el usuario: {e}")

# Función para registrar un nuevo libro
def registrar_libro():
    try:
        id_libro = max([libro["id"] for libro in libros]) + 1
        titulo = input("Ingrese el título del libro: ").strip()
        autor = input("Ingrese el autor: ").strip()
        isbn = input("Ingrese el ISBN: ").strip()
        paginas = int(input("Ingrese el número de páginas: "))
        cantidad = int(input("Ingrese la cantidad de copias del libro que registrará : "))
        libros.append({
            "id": id_libro,
            "titulo": titulo,
            "autor": autor,
            "ISBN": isbn,
            "paginas": paginas,
            "cantidad_disponible": cantidad
        })
        print(f"Libro '{titulo}' registrado exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al registrar el libro: {e}")

# Función para mostrar libros disponibles
def mostrar_libros_disponibles():
    print("\n Libros disponibles:")
    for libro in libros:
        print(f"{libro['id']}. {libro['titulo']} ({libro['cantidad_disponible']} disponibles)")

# Función para préstamo de libro
def prestar_libro(usuario):
    mostrar_libros_disponibles()
    try:
        id_libro = int(input("Ingrese el ID del libro que desea prestar: "))
        libro = next((l for l in libros if l["id"] == id_libro), None)
        if libro and libro["cantidad_disponible"] > 0:
            libro["cantidad_disponible"] -= 1
            usuario["libros"].append(libro["id"])
            print(f"Libro '{libro['titulo']}' prestado a {usuario['nombre']} {usuario['apellido']}.")
        else:
            print("No se puede prestar este libro (no existe o no hay stock).")
    except Exception as e:
        print(f"Error al prestar libro: {e}")

# Función para devolver un libro
def devolver_libro(usuario):
    if not usuario["libros"]:
        print("ℹ️ No hay libros para devolver.")
        return
    print("\n Libros prestados:")
    for i, id_libro in enumerate(usuario["libros"], 1):
        libro = next((l for l in libros if l["id"] == id_libro), None)
        if libro:
            print(f"{i}. {libro['titulo']}")
    try:
        opcion = int(input("Seleccione el número del libro a devolver: "))
        id_devuelto = usuario["libros"].pop(opcion - 1)
        libro = next((l for l in libros if l["id"] == id_devuelto), None)
        if libro:
            libro["cantidad_disponible"] += 1
            print(f" Libro '{libro['titulo']}' devuelto.")
        else:
            print(" El libro no existe en el sistema.")
            registrar = input("¿Desea registrar este libro? (s/n): ").lower()
            if registrar == "s":
                registrar_libro()
    except Exception as e:
        print(f"Error en la devolución: {e}")

# Menú principal
def menu():
    while True:
        print("\n SISTEMA DE BIBLIOTECAS")
        print("1 - Buscar usuario por RUT")
        print("2 - Registrar nuevo usuario")
        print("3 - Registrar nuevo libro")
        print("4 - Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            rut = input("Ingrese el RUT: ").strip()
            usuario = buscar_usuario(rut)
            if usuario:
                print(f" Usuario: {usuario['nombre']} {usuario['apellido']}")
                while True:
                    print("\n1 - Prestar libro")
                    print("2 - Devolver libro")
                    print("3 - Volver")
                    sub = input("Opción: ").strip()
                    if sub == "1":
                        prestar_libro(usuario)
                    elif sub == "2":
                        devolver_libro(usuario)
                    elif sub == "3":
                        break
                    else:
                        print("Opción inválida.")
            else:
                print(" Usuario no encontrado.")
                crear = input("¿Desea registrarlo? (s/n): ").lower()
                if crear == "s":
                    registrar_usuario()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            registrar_libro()
        elif opcion == "4":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print(" Opción inválida.")

# Iniciar el sistema
menu()