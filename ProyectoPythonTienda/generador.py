import os

# Directorio de salida para los archivos SQL
directorio_salida = 'Scripts'

# Asegúrate de que el directorio exista
if not os.path.exists(directorio_salida):
    os.makedirs(directorio_salida)

# Función para generar los inserts y escribir en el archivo
def generar_inserts(archivo_salida, inserts):
    with open(archivo_salida, 'w') as archivo:
        archivo.writelines(inserts)

# Bucle para la tabla cliente
inserts_cliente = [f"INSERT INTO cliente (nombre, cif, direccion) VALUES ('cliente{i}', 'CIF{i}', 'Direccion{i}');\n" for i in range(1, 101)]
generar_inserts(os.path.join(directorio_salida, 'insert_cliente.sql'), inserts_cliente)

# Bucle para la tabla modelo
inserts_modelo = [f"INSERT INTO modelo (descripcion) VALUES ('DescripcionModelo{i}');\n" for i in range(1, 101)]
generar_inserts(os.path.join(directorio_salida, 'insert_modelo.sql'), inserts_modelo)

# Bucle para la tabla marca
inserts_marca = [f"INSERT INTO marca (descripcion) VALUES ('DescripcionMarca{i}');\n" for i in range(1, 101)]
generar_inserts(os.path.join(directorio_salida, 'insert_marca.sql'), inserts_marca)

# Bucle para la tabla marca_modelo (relaciones)
inserts_relacion = [f"INSERT INTO marca_modelo (id_marca, id_modelo) VALUES ({i}, {i});\n" for i in range(1, 101)]
generar_inserts(os.path.join(directorio_salida, 'insert_marca_modelo.sql'), inserts_relacion)

# Bucle para la tabla producto
inserts_producto = [f"INSERT INTO producto (descripcion, precio, id_marca_modelo, fecha_creacion) VALUES ('DescripcionProducto{i}', {i * 10.5}, {i}, CURRENT_DATE);\n" for i in range(1, 101)]
generar_inserts(os.path.join(directorio_salida, 'insert_producto.sql'), inserts_producto)

# Bucle para la tabla ventas
inserts_venta = [f"INSERT INTO ventas (id_producto, cantidad, id_cliente, fecha_inicio_compra, fecha_fin_compra) VALUES ({i}, {i * 2}, {i}, CURRENT_DATE, CURRENT_DATE + INTERVAL '{i} days');\n" for i in range(1, 101)]
generar_inserts(os.path.join(directorio_salida, 'insert_ventas.sql'), inserts_venta)

# Bucle para la tabla reposicion
inserts_reposicion = [f"INSERT INTO reposicion (id_producto, cantidad, fecha_inicio_reposicion, fecha_fin_reposicion) VALUES ({i}, {i * 3}, CURRENT_DATE, CURRENT_DATE + INTERVAL '{i} days');\n" for i in range(1, 101)]
generar_inserts(os.path.join(directorio_salida, 'insert_reposicion.sql'), inserts_reposicion)

# Bucle para la tabla inventario
inserts_inventario = [f"INSERT INTO inventario (id_producto, fecha_actualizacion, cantidad_existente, cantidad_entrante, cantidad_saliente, id_venta, id_reposicion) VALUES ({i}, CURRENT_DATE, 50, {i * 5}, 1, {i}, {i});\n" for i in range(1, 101)]
generar_inserts(os.path.join(directorio_salida, 'insert_inventario.sql'), inserts_inventario)

