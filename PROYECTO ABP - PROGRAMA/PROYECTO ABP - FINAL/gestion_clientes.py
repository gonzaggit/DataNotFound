# gestion_clientes.py

# Importa la función para conectarnos a la base de datos
from conexion_base_datos import obtener_conexion

# ==== FUNCIONES CRUD ====

# Obtener clientes registrados en la base de datos
def listar_clientes():
    conexion = obtener_conexion()  # Se establece la conexión
    cursor = conexion.cursor(dictionary=True)  # Se usa formato diccionario para acceder por nombre de columna
    cursor.execute("SELECT * FROM clientes")  # Consulta SQL
    clientes = cursor.fetchall()  # Trae todos los resultados
    conexion.close()  # Cierra la conexión
    return clientes  # Devuelve la lista de clientes

# Añadir nuevo cliente a la base de datos
def agregar_cliente(cuit_cuil, nombre_razonsocial, correo_electronico):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    query = f"""
    INSERT INTO clientes (cuit_cuil, nombre_razonsocial, correo_electronico)
    VALUES ('{cuit_cuil}', '{nombre_razonsocial}', '{correo_electronico}')
    """
    cursor.execute(query)
    conexion.commit()
    conexion.close()
    print("Cliente agregado con éxito.")
    
# Modifica cliente existente
def modificar_cliente(nuevo_cuit_cuil, nuevo_nombre_razonsocial, nuevo_correo_electronico):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    # Actualiza la razón social y correo 
    cursor.execute(
        "UPDATE clientes SET nombre_razonsocial = %s, correo_electronico = %s WHERE cuit_cuil = %s",
        (nuevo_nombre_razonsocial, nuevo_correo_electronico, nuevo_cuit_cuil)
    )
    conexion.commit()
    conexion.close()
    print("Cliente modificado con éxito.")

# Elmina cliente
def eliminar_cliente(cuit_cuil):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM clientes WHERE cuit_cuil = %s", (cuit_cuil,))
    conexion.commit()
    conexion.close()
    print("Cliente eliminado con éxito.")

# ==== MENÚ INTERACTIVO ====

# Función que contiene el menú para gestionar clientes, e invoca las funciones anteriores
def opcion_clientes():
    while True:
        print("\n==== Gestionar Clientes ====")
        print("1. Ver Clientes")
        print("2. Agregar Cliente")
        print("3. Modificar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al Menu Principal")

        subopcion = input("Seleccione una opción: ")

        if subopcion == "1":
            # Llama a la función que lista los clientes
            clientes = listar_clientes()
            if clientes:
                for c in clientes:
                    print(c)  # Imprime cada cliente
            else:
                print("No hay clientes registrados.")
        elif subopcion == "2":
    # Solicita los datos del nuevo cliente y los pasa a la función agregar_cliente
            cuit_cuil = input("CUIT o CUIL según corresponda: ")
            razon = input("Razón social: ")
            correo = input("Correo electrónico: ")
            agregar_cliente(cuit_cuil, razon, correo)

        elif subopcion == "3":
            # Solicita CUIT y nuevos datos, luego llama a la función para modificar
            nuevo_cuit_cuil = input("CUIT del cliente a modificar: ")
            nuevo_nombre_razonsocial = input("Nueva razón social: ")
            nuevo_correo_electronico = input("Nuevo correo: ")
            modificar_cliente(nuevo_cuit_cuil, nuevo_nombre_razonsocial, nuevo_correo_electronico)


        elif subopcion == "4":
            # Solicita CUIT del cliente a eliminar
            cuit = input("CUIT del cliente a eliminar: ")
            eliminar_cliente(cuit)

        elif subopcion == "5":
            # Vuelve al menú principal
            break
        else:
            print("Opción inválida, intente nuevamente.")
