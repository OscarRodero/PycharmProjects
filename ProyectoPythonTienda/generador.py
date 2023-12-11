import os

# Función para generar los inserts y escribir en el archivo
def generar_inserts(archivo_salida, tabla, valores):
    with open(archivo_salida, 'w') as archivo:
        for i in range(1, 1001):
            insert_command = f"INSERT INTO {tabla} VALUES ({i}, {valores[i-1]});"
            if i < 1000:
                insert_command += "\n"
            archivo.write(insert_command)

# Generar datos ficticios para las relaciones entre marca y modelo
relaciones_marcamodelo = [(i, i) for i in range(1, 1001)]

# Generar inserts para la tabla cliente
archivo_salida = 'Scripts/insert_cliente.sql'
valores_cliente = [(f"'cliente{i}'", f"'CIF{i}'", f"'Direccion{i}'") for i in range(1, 1001)]
generar_inserts(archivo_salida, 'cliente', valores_cliente)

# Generar inserts para la tabla modelo
archivo_salida = 'Scripts/insert_modelo.sql'
valores_modelo = [(f"'DescripcionModelo{i}'",) for i in range(1, 1001)]
generar_inserts(archivo_salida, 'modelo', valores_modelo)

# Generar inserts para la tabla marca
archivo_salida = 'Scripts/insert_marca.sql'
valores_marca = [(f"'DescripcionMarca{i}'",) for i in range(1, 1001)]
generar_inserts(archivo_salida, 'marca', valores_marca)

# Generar inserts para la tabla marca_modelo
archivo_salida = 'Scripts/insert_marcamodelo.sql'
generar_inserts(archivo_salida, 'marca_modelo', relaciones_marcamodelo)
