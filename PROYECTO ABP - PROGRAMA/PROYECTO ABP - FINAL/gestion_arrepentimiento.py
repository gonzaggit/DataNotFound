# gestion boton de arrepentimiento
from conexion_base_datos import obtener_conexion
from datetime import datetime, time

# Mostrar ventas activas del cliente (estado = 1)
def obtener_ventas_cliente(cuit_cuil):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT v.id_ventas, v.fecha_venta, v.hora_venta, d.ciudad
        FROM ventas v
        JOIN destinos d ON v.id_destino = d.id_destino
        WHERE v.cuit_cuil = %s AND v.id_estado = 1
    """, (cuit_cuil,))
    ventas = cursor.fetchall()
    conexion.close()
    return ventas

# Cambiar el estado de la venta a anulada (id_estado = 2)
def anular_venta(id_ventas):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE ventas SET id_estado = 2 WHERE id_ventas = %s", (id_ventas,))
    conexion.commit()
    conexion.close()
    print("La venta fue anulada con éxito.")

# Menú del botón de arrepentimiento
def opcion_arrepentimiento():
    print("\n==== Botón de Arrepentimiento ====")
    cuit_cuil = input("Ingrese su CUIT o CUIL: ")

    ventas = obtener_ventas_cliente(cuit_cuil)
    if not ventas:
        print("No se encontraron ventas activas para el CUIT o CUIL ingresado.")
        return

    print("Ventas activas encontradas:")
    for i, venta in enumerate(ventas, 1):
        print(f"{i}. ID Venta: {venta['id_ventas']} | Ciudad: {venta['ciudad']} | Fecha: {venta['fecha_venta']} {venta['hora_venta']}")

    seleccion = input("Seleccione el número de la venta que desea anular: ")

    try:
        seleccion = int(seleccion) - 1
        venta_seleccionada = ventas[seleccion]
    except (ValueError, IndexError):
        print("Selección inválida.")
        return

    fecha = venta_seleccionada["fecha_venta"]
    hora = venta_seleccionada["hora_venta"]

    # Verificar y convertir la hora si es timedelta
    if isinstance(hora, time):
        hora_convertida = hora
    else:
        # Suponemos que es timedelta
        segundos_totales = int(hora.total_seconds())
        horas = segundos_totales // 3600
        minutos = (segundos_totales % 3600) // 60
        segundos = segundos_totales % 60
        hora_convertida = time(horas, minutos, segundos)

    # Combinar fecha y hora
    fecha_venta = datetime.combine(fecha, hora_convertida)

    # Calcular diferencia en minutos
    diferencia = (datetime.now() - fecha_venta).total_seconds() / 60

    # Verificación del "arrepentimiento" dentro de los 10 días (simulados como 5 minutos)
    if diferencia <= 5:
        anular_venta(venta_seleccionada["id_ventas"])
    else:
        print("No se puede anular. Ya pasaron más de 10 días desde la compra.")
