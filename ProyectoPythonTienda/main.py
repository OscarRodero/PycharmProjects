from Clases import *
import os
import psycopg2
from psycopg2 import sql

class PostgreSQLConnection:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Conexión exitosa")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Desconexión exitosa")

    def execute_query(self, query, parameters=None):
        if not self.connection:
            print("Error: No hay conexión a la base de datos.")
            return

        try:
            with self.connection.cursor() as cursor:
                if parameters:
                    cursor.execute(query, parameters)
                else:
                    cursor.execute(query)

                result = cursor.fetchall()
                return result
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None

# Ejemplo de uso
if __name__ == "__main__":
    # Configuración de la conexión
    db_config = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'root',
        'host': 'localhost',
        'port': '5432',
    }

    # Crear una instancia de la clase PostgreSQLConnection
    db_connection = PostgreSQLConnection(**db_config)

    # Conectar a la base de datos
    db_connection.connect()

    # Ejecutar una consulta
    query = 'SELECT * FROM "public"."Inventario";'
    result = db_connection.execute_query(query)

    # Imprimir el resultado
    if result:
        print(result)

    # Desconectar de la base de datos
    db_connection.disconnect()