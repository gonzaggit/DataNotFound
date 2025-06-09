#consultas SELECT
SELECT* FROM clientes; 

SELECT *
FROM ventas
WHERE fecha_venta = '2025-06-03';

#multitabla: Buscamos ultima venta registrada por cliente, unimos tabla clientes y ventas, y agrupamos por cliente (utilizando MAX para mostrar la fecha mas reciente)

SELECT 
  clientes.cuit_cuil, clientes.nombre_razonsocial,
  MAX(ventas.fecha_venta) AS ultima_fecha_venta
FROM clientes
INNER JOIN ventas ON clientes.cuit_cuil = ventas.cuit_cuil
GROUP BY clientes.cuit_cuil, clientes.nombre_razonsocial;

#Mostramos los destinos donde la ciudad empieza con S
SELECT *
FROM destinos
WHERE ciudad LIKE 'S%';

#contamos cuantas ventas hubo para cada pais, unimos tablas ventas y destinos, unimos destinos con paises, agrupamos por nombre de pais para ver cantidad de ventas
SELECT paises.nombre_pais,
COUNT(ventas.id_ventas) AS cantidad_ventas
FROM ventas 
INNER JOIN destinos ON ventas.id_destino = destinos.id_destino
INNER JOIN paises ON destinos.id_pais = paises.id_pais
GROUP BY paises.nombre_pais;
