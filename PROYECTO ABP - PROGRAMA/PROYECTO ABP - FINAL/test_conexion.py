from conexion_base_datos import obtener_conexion

conexion = obtener_conexion()
if conexion:
    print("✅ Conexión exitosa a la base de datos.")
    conexion.close()
else:
    print("❌ Error en la conexión.")
