# consultas.py

from conexion_base_datos import obtener_conexion

def mostrar_clientes():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conexion.close()
    return clientes

def mostrar_destinos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT d.id_destino, d.ciudad, d.costo, p.nombre_pais
        FROM destinos d
        JOIN paises p ON d.id_pais = p.id_pais
    """)
    destinos = cursor.fetchall()
    conexion.close()
    return destinos

def buscar_ventas_por_cliente(cuit):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT v.id_ventas, v.fecha_venta, d.ciudad, ev.descripcion_estado
        FROM ventas v
        JOIN destinos d ON v.id_destino = d.id_destino
        JOIN estado_venta ev ON v.id_estado = ev.id_estado
        WHERE v.cuit_cuil = %s
    """, (cuit,))
    ventas = cursor.fetchall()
    conexion.close()
    return ventas

def buscar_ventas_por_destino(id_destino):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT v.id_ventas, v.fecha_venta, c.nombre_razonsocial, ev.descripcion_estado
        FROM ventas v
        JOIN clientes c ON v.cuit_cuil = c.cuit_cuil
        JOIN estado_venta ev ON v.id_estado = ev.id_estado
        WHERE v.id_destino = %s
    """, (id_destino,))
    ventas = cursor.fetchall()
    conexion.close()
    return ventas

def buscar_ventas_por_estado(id_estado):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT v.id_ventas, v.fecha_venta, c.nombre_razonsocial, d.ciudad
        FROM ventas v
        JOIN clientes c ON v.cuit_cuil = c.cuit_cuil
        JOIN destinos d ON v.id_destino = d.id_destino
        WHERE v.id_estado = %s
    """, (id_estado,))
    ventas = cursor.fetchall()
    conexion.close()
    return ventas

# Menú de consultas
def opcion_consulta():
    while True:
        print("\n==== Consultas ====")
        print("1. Ver clientes")
        print("2. Ver destinos")
        print("3. Ventas por cliente")
        print("4. Ventas por destino")
        print("5. Ventas por estado")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clientes = mostrar_clientes()
            for c in clientes:
                print(c)

        elif opcion == "2":
            destinos = mostrar_destinos()
            for d in destinos:
                print(d)

        elif opcion == "3":
            cuit = input("Ingrese el CUIT del cliente: ")
            ventas = buscar_ventas_por_cliente(cuit)
            for v in ventas:
                print(v)

        elif opcion == "4":
            id_destino = input("Ingrese el ID del destino: ")
            ventas = buscar_ventas_por_destino(id_destino)
            for v in ventas:
                print(v)

        elif opcion == "5":
            print("1. Procesada\n2. Anulada")
            estado = input("Ingrese el número del estado: ")
            ventas = buscar_ventas_por_estado(estado)
            for v in ventas:
                print(v)

        elif opcion == "6":
            break

        else:
            print("Opción inválida.")
