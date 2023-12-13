import os
import logging
import psycopg2
import subprocess
from psycopg2 import sql
from Clases import *
from datetime import datetime

log_directory = 'Logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_filename = f'Logs/{datetime.now().strftime("%d-%m-%Y")}.log'
logging.basicConfig(filename=log_filename, level=logging.INFO)
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

def ejecutar_generador():
    try:
        subprocess.run(["python", "generador.py"], check=True)
        print("Script generador.py ejecutado con éxito.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el script generador.py: {e}")
def cargarDatos():
    try:
        ejecutar_generador()
        script_file = os.path.join('Scripts', 'insert_cliente.sql')

        with open(script_file, 'r') as file:
            script_content = file.read()

        db_connection.execute_query(script_content)
        logging.info("Carga de datos exitosa.")

    except Exception as e:
        error_message = f"Error al cargar datos: {e}"
        logging.error(error_message)
        print(error_message)


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
    cargarDatos()

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