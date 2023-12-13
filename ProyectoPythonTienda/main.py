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
def imprimir_menu():
    print("1. Consultar ventas por cliente")
    print("2. Salir")
    opcion = input("\n"+"Seleccione una opción: ")
    return opcion

if __name__ == "__main__":
    db_config = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'root',
        'host': 'localhost',
        'port': '5432',
    }

    db_connection = PostgreSQLConnection(**db_config)
    db_connection.connect()

    while True:
        choice = imprimir_menu()
        if choice == '1':
            try:
                cliente_id = int(input("Ingrese el ID del cliente: "))
            except ValueError:
                print("Error: Ingrese un número válido para el ID del cliente.")
                continue
            query = sql.SQL('SELECT * FROM "public"."ventas" WHERE cliente_id = {}').format(sql.Literal(cliente_id))
            result = db_connection.execute_query(query)
            if result:
                for r in result:
                    obj_venta = Venta(*r)
                    print(obj_venta)
            else:
                print("No se encontraron ventas para el cliente especificado.")
        elif choice == '2':
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

    db_connection.disconnect()