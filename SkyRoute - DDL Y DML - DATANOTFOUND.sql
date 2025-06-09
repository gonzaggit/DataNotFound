#Creación sentencias DDL. Creamos base de datos, y todas las tablas coincidiendo con el DER
CREATE DATABASE IF NOT EXISTS skyroute;
USE skyroute;

#tabla destinos
CREATE TABLE destinos (
id_destino INT AUTO_INCREMENT PRIMARY KEY,
id_pais INT,
ciudad VARCHAR (50),
costo FLOAT
);

#Tabla ventas
CREATE TABLE ventas (
id_ventas INT AUTO_INCREMENT PRIMARY KEY,
id_destino INT,
cuit_cuil BIGINT, #para que contemple 11 dígitos 
id_estado INT,
fecha_venta DATE,
hora_venta TIME
);

#Tabla clientes
CREATE TABLE clientes (
cuit_cuil BIGINT PRIMARY KEY,
id_tipo_cliente INT,
nombre_razonsocial VARCHAR(50),
correo_electronico VARCHAR(50)
);

#tabla paises
CREATE TABLE paises (
id_pais INT AUTO_INCREMENT PRIMARY KEY,
nombre_pais VARCHAR(50)
); 

#tabla tipo de cliente: agregamos restricción ya que la id_tipo_cliente solo puede ser 1 (persona) o 2 (empresa)
CREATE TABLE tipo_de_cliente (
    id_tipo_cliente INT PRIMARY KEY,
    descripcion_cliente VARCHAR(50),
    CONSTRAINT check_tipo_cliente CHECK (id_tipo_cliente IN (1, 2))
); 

#Tabla estado de venta: agregamos restricción ya que la id_estado solo puede ser 1 (procesada) o 2 (anulada)
CREATE TABLE estado_venta (
    id_estado INT PRIMARY KEY,
    descripcion_estado VARCHAR(50),
    CONSTRAINT check_estado CHECK (id_estado IN (1, 2)) #1 procesada, 2 anulada 
);

#Restricciones: Fue mas sencillo primero crear todas las tablas y a posterior agregar las restricciones en este caso, las FK, para poder respetar los ordenes lógicos de asociaciones entre tablas.
ALTER TABLE ventas
ADD CONSTRAINT fk_destino
FOREIGN KEY (id_destino) REFERENCES destinos(id_destino);
ALTER TABLE ventas
ADD CONSTRAINT fk_cuit_cuil
FOREIGN KEY (cuit_cuil) REFERENCES clientes(cuit_cuil);
ALTER TABLE ventas
ADD CONSTRAINT fk_id_estado
FOREIGN KEY (id_estado) REFERENCES estado_venta(id_estado);

ALTER TABLE destinos
ADD CONSTRAINT fk_id_pais
FOREIGN KEY (id_pais) REFERENCES paises(id_pais);

ALTER TABLE clientes 
ADD CONSTRAINT fk_id_tipo_cliente
FOREIGN KEY (id_tipo_cliente) REFERENCES tipo_de_cliente(id_tipo_cliente);

-- sentencias DML agregar datos: Agregamos datos inventados para probar las tablas y consultas
INSERT INTO paises (nombre_pais) 
VALUES ('Argentina'), 
       ('Brasil'), 
       ('Uruguay');
       
INSERT INTO destinos (id_pais, ciudad, costo) 
VALUES (1, 'Buenos Aires', 60000.00), 
       (2, 'Sao Paulo', 350000.00), 
       (2, 'Florianopolis', 285000.00),
       (1, 'Salta', 40000.00);
	
INSERT INTO tipo_de_cliente (id_tipo_cliente, descripcion_cliente)
VALUES (1, 'Persona'),
(2, 'Empresa');

       
INSERT INTO clientes (cuit_cuil, id_tipo_cliente, nombre_razonsocial, correo_electronico) 
VALUES (27409288001, 1, 'Jimena Theaux', 'jimenatheaux@gmail.com'), 
       (20345678901, 2, 'Arcor', 'Arcor.recursoshumanos@gmail.com'), 
       (20456789012, 1, 'Valentina Gesto', 'vale.gesto@gmail.com');
	

INSERT INTO estado_venta (id_estado, descripcion_estado) 
VALUES (1, 'Procesada'), 
       (2, 'Anulada');
	
INSERT INTO ventas (id_destino, cuit_cuil, id_estado, fecha_venta) 
VALUES (1, 27409288001, 1, '2025-06-01'), 
       (2, 20345678901, 2, '2025-06-03'), 
       (3, 20456789012, 1, '2025-06-05');       