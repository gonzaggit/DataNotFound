#gestion_destinos.py

from conexion_base_datos import obtener_conexion

# Mostrar todos los destinos
def listar_destinos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)  #Devuelve datos en forma de diccionario (clave: noombre de columna; valor= dato)
    cursor.execute("""
        SELECT d.id_destino, d.ciudad, d.costo, p.nombre_pais
        FROM destinos d
        JOIN paises p ON d.id_pais = p.id_pais
    """)
    destinos = cursor.fetchall()
    conexion.close()
    return destinos

# Agregar un nuevo destino
def agregar_destino(id_pais, ciudad, costo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO destinos (id_pais, ciudad, costo) VALUES (%s, %s, %s)",
        (id_pais, ciudad, costo)
    )
    conexion.commit()
    conexion.close()
    print("Destino agregado con éxito.")

# Modificar la ciudad y costo de un destino
def modificar_destino(id_destino, nueva_ciudad, nuevo_costo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE destinos SET ciudad = %s, costo = %s WHERE id_destino = %s",
        (nueva_ciudad, nuevo_costo, id_destino)
    )
    conexion.commit()
    conexion.close()
    print("Destino modificado con éxito.")

# Eliminar un destino por ID
def eliminar_destino(id_destino):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM destinos WHERE id_destino = %s", (id_destino,))
    conexion.commit()
    conexion.close()
    print("Destino eliminado con éxito.")

# Menú de destinos
def opcion_destinos():
    while True:
        print("\n==== Gestión de Destinos ====")
        print("1. Ver destinos")
        print("2. Agregar destino")
        print("3. Modificar destino")
        print("4. Eliminar destino")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            destinos = listar_destinos()
            for d in destinos:
                print(f"ID: {d['id_destino']} | Ciudad: {d['ciudad']} | País: {d['nombre_pais']} | Costo: ${d['costo']}")

        elif opcion == "2":
            id_pais = input("ID del país: ")
            ciudad = input("Nombre de la ciudad: ")
            costo = input("Costo del pasaje: ")
            agregar_destino(id_pais, ciudad, costo)

        elif opcion == "3":
            id_destino = input("ID del destino a modificar: ")
            nueva_ciudad = input("Nuevo nombre de ciudad: ")
            nuevo_costo = input("Nuevo costo: ")
            modificar_destino(id_destino, nueva_ciudad, nuevo_costo)

        elif opcion == "4":
            id_destino = input("ID del destino a eliminar: ")
            eliminar_destino(id_destino)

        elif opcion == "5":
            break

        else:
            print("Opción inválida, intente nuevamente.")
