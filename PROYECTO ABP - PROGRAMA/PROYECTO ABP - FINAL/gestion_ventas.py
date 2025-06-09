# gestion_ventas.py

from conexion_base_datos import obtener_conexion

# Registrar una nueva venta con estado "Procesada" (id_estado = 1)
def registrar_venta(cuit_cuil, id_destino, fecha_venta, hora_venta):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO ventas (id_destino, cuit_cuil, id_estado, fecha_venta, hora_venta) VALUES (%s, %s, %s, %s, %s)",
        (id_destino, cuit_cuil, 1, fecha_venta, hora_venta)  # estado 1 = procesada
    )
    conexion.commit()
    conexion.close()
    print("Venta registrada con éxito.")

# Mostrar todas las ventas (con ID, cliente, destino y estado)
def listar_ventas():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT v.id_ventas, v.fecha_venta, c.nombre_razonsocial, d.ciudad, ev.descripcion_estado
        FROM ventas v
        JOIN clientes c ON v.cuit_cuil = c.cuit_cuil
        JOIN destinos d ON v.id_destino = d.id_destino
        JOIN estado_venta ev ON v.id_estado = ev.id_estado
    """)
    ventas = cursor.fetchall()
    conexion.close()
    return ventas

# Cambiar el estado de una venta (por ejemplo, a anulada)
def modificar_estado_venta(id_ventas, nuevo_estado):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE ventas SET id_estado = %s WHERE id_ventas = %s", (nuevo_estado, id_ventas))
    conexion.commit()
    conexion.close()
    print("Estado de venta actualizado.")

# Eliminar una venta por ID
def eliminar_venta(id_ventas):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM ventas WHERE id_ventas = %s", (id_ventas,))
    conexion.commit()
    conexion.close()
    print("Venta eliminada con éxito.")

# Menú de ventas
def opcion_ventas():
    while True:
        print("\n==== Gestión de Ventas ====")
        print("1. Registrar nueva venta")
        print("2. Ver historial de ventas")
        print("3. Cambiar estado de una venta")
        print("4. Eliminar venta")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cuit = input("CUIT del cliente: ")
            destino = input("ID del destino: ")
            fecha = input("Fecha de venta (YYYY-MM-DD): ")
            hora = input("Hora de venta (HH:MM:SS): ")
            registrar_venta(cuit, destino, fecha, hora)

        elif opcion == "2":
            ventas = listar_ventas()
            for v in ventas:
                print(f"ID: {v['id_ventas']} | Cliente: {v['nombre_razonsocial']} | "
                      f"Destino: {v['ciudad']} | Fecha: {v['fecha_venta']} | Estado: {v['descripcion_estado']}")

        elif opcion == "3":
            id_venta = input("ID de la venta a modificar: ")
            print("1. Procesada\n2. Anulada")
            nuevo_estado = input("Ingrese el número del nuevo estado: ")
            modificar_estado_venta(id_venta, nuevo_estado)

        elif opcion == "4":
            id_venta = input("ID de la venta a eliminar: ")
            eliminar_venta(id_venta)

        elif opcion == "5":
            break
        else:
            print("Opción inválida, intente nuevamente.")
