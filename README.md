Proyecto:
SkyRoute S.R.L es un sistema desarrollado como parte de un proyecto academico,
con el propósito de simular el funcionamiento de una agencia de pasajes aéreos.
Aquí se pueden registrar diferentes tipos de clientes, tanto empresas como
personas físicas, gestionar destinos con sus respectivos costos y asociar cada
venta a un cliente y destino específico.
Además, incorpora la función del “botón de arrepentimiento”, que simula el
derecho del usuario a cancelar una compra dentro de un plazo determinado, en
línea con la normativa de defensa al consumidor.

Integrantes:
Cabrera, Gonzalo (41501046)
Gesto, Valentina (41893604)
Guevara, Gonzalo (38802553)
Herrera, Bruno (46592052)
Theaux, Jimena (40928800)

Contenido del repositorio:
skyroute/

├── config.py # Configuración de conexión a la base de datos
├── conexion_base_datos.py  # Conexión y operaciones con MySQL
├── main.py  # Archivo principal con menú de opciones
├── gestion_clientes.py  # Alta, baja, modificación, listado de clientes
├── gestion_destinos.py   # Alta, baja, modificación, listado de destinos
├── gestion_ventas.py  # Registrar ventas y botón de arrepentimiento
├── gestion_arrepentimiento.py  #Anular venta y/o ver su estado
├── consultas.py  #Consultar sobre la información de la base de datos
├── test_conexion.py  #Comprobar la conexion a la base de datos
├── poster ABP #Poster del proyecto ABP
├── Documento Proyecto Final ABP  #Documento final ABP
├── Ética - Proyecto ABP.pdf  #Informe Ética
├── SkyRoute - DDL Y DML - DATANOTFOUND.sql  #Creación y modificación de base de datos
├── SkyRoute - Consultas SELECT - DATANOTFOUND.sql #Consultas de base de datos
├── Video Proyecto ABP - DataNotFound (Grupo 33) #Presentación final
└── README.MD   # Documentación del proyecto

Requisitos:
Python version 3.9 en adelante y un servidor de base de datos relacional (ej.: MySQL WorkBench). 

Pasos a seguir:
1. Descargar el archivo SkyRoute.zip y SkyRoute.sql.
2. Crear la base de datos ejecutando el archivo .sql provisto.
3. Abrir todos los archivos .py (carpeta proyecto ABP - programa).
4. Modificar el archivo config.py, configurando los datos de conexión.
5. Ejecutar el archivo main.py.
6. Seguir las instrucciones indicadas.
