import os
import logging
import psycopg2
import subprocess
from psycopg2 import sql
from Clases import *
from datetime import datetime

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
        except Exception as e:
            logging.error(f"Error al conectar a la base de datos: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, parameters=None):
        db_connection.connect()
        if not self.connection:
            logging.error("Error: No hay conexión a la base de datos.")
            return
        try:
            with self.connection.cursor() as cursor:
                if parameters:
                    cursor.execute(query, parameters)
                    self.connection.commit()
                else:
                    cursor.execute(query)
                    self.connection.commit()
                # Si la consulta es un INSERT, UPDATE o DELETE, no intentamos realizar fetch
                if query.strip().upper().startswith(('INSERT', 'UPDATE', 'DELETE')):
                    return None
                else:
                    result = cursor.fetchall()
                    return result
        except psycopg2.Error as e:
            logging.error(f"Error al ejecutar la consulta: {e}")
            return None
        except Exception as e:
            logging.error(e)
        finally:
            db_connection.disconnect()

def setup_logger():
    # Configurar el logger
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, f"{datetime.now().strftime('%d-%m-%Y')}.log")
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ejecutar_generador():
    try:
        subprocess.run(["python", "generador.py"], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error al ejecutar el script generador.py: {e}")

def cargarDatos():
    logging.info("Primera ejecución del programa, cargando datos...")
    db_connection.connect()
    scripts = ['insert_cliente.sql', 'insert_modelo.sql', 'insert_marca.sql', 'insert_marca_modelo.sql',
               'insert_producto.sql', 'insert_ventas.sql', 'insert_reposicion.sql', 'insert_inventario.sql']
    try:
        for archivo in scripts:
            with open(os.path.join('Scripts', archivo), 'r') as file:
                script_content = file.read()
            result = db_connection.execute_query(script_content)
            if result is not None:
                logging.info(f"Resultado de la ejecución: {result}")

    except Exception as e:
        error_message = f"Error al cargar datos: {e}"
        logging.error(error_message)
        print(error_message)
    finally:
        db_connection.disconnect()

def imprimirMenuPrincipal():
    print("1. Consultar ventas relacionadas con un cliente.")
    print("2. Ver la cantidad total que un cliente ha gastado.")
    print("3. Revisar la última venta del historial de un cliente.")
    print("4. Revisar la primera venta del historial de un cliente.")
    print("5. Consultar las existencias de un producto.")
    print("6. Salir")
    opcion = input("\n" + "Seleccione una opción: ")
    return opcion

if __name__ == '__main__':
    try:
        setup_logger()
        db_config = {
            'dbname': 'postgres',
            'user': 'postgres',
            'password': 'postgres',
            'host': 'localhost',
            'port': '5432',
        }
        db_connection = PostgreSQLConnection(**db_config)

        if not os.path.exists('datos_cargados.txt'):
            ejecutar_generador()
            cargarDatos()
            with open('datos_cargados.txt', 'w') as file:
                file.write('Cargados\n')

        salir = False
        logging.info("Iniciado el programa")
        while not salir:
            opcion = imprimirMenuPrincipal()
            if opcion == '1':
                logging.info("Se ha seleccionado la opción 1")
                try:
                    cliente_id = input("Ingrese el ID del cliente: ")
                    query_ventas_cliente = "SELECT * FROM ventas WHERE id_cliente = %s;"
                    parameters_ventas_cliente = (cliente_id,)
                    results_ventas_cliente = db_connection.execute_query(query_ventas_cliente, parameters_ventas_cliente)

                    if results_ventas_cliente:
                        print(f"Ventas asociadas al cliente con ID {cliente_id}:")
                        for result_venta_cliente in results_ventas_cliente:
                            venta_cliente = Venta(result_venta_cliente[0], result_venta_cliente[1], result_venta_cliente[2], result_venta_cliente[3], result_venta_cliente[4], result_venta_cliente[5])
                            print(venta_cliente)
                    else:
                        print(f"No hay ventas para el cliente con ID {cliente_id}")

                except Exception as e:
                    logging.error(f"Error al consultar ventas: {e}")
            elif opcion == '2':
                logging.info("Se ha seleccionado la opción 2")
                try:
                    cliente_id = input("Ingrese el ID del cliente: ")
                    query_ventas = "SELECT id_producto, cantidad FROM ventas WHERE id_cliente = %s;"
                    parameters_ventas = (cliente_id,)
                    results_ventas = db_connection.execute_query(query_ventas, parameters_ventas)

                    if results_ventas:
                        total_gastado = 0
                        for result_venta in results_ventas:
                            id_producto = result_venta[0]
                            cantidad = result_venta[1]
                            query_precio = "SELECT precio FROM producto WHERE id = %s;"
                            parameters_precio = (id_producto,)
                            result_precio = db_connection.execute_query(query_precio, parameters_precio)
                            if result_precio:
                                precio_producto = result_precio[0][0]
                                total_gastado += precio_producto * cantidad
                            else:
                                print(f"No se encontró el precio para el producto con ID {id_producto}")

                        print(f"El cliente con ID {cliente_id} ha gastado un total de ${total_gastado}")
                    else:
                        print(f"No hay ventas para el cliente con ID {cliente_id}")

                except Exception as e:
                    logging.error(f"Error al calcular el total gastado: {e}")
            elif opcion == '3':
                logging.info("Se ha seleccionado la opción 3")
                try:
                    cliente_id = input("Ingrese el ID del cliente: ")
                    query_ultima_venta = "SELECT * FROM ventas WHERE id_cliente = %s ORDER BY fecha_inicio_compra DESC LIMIT 1;"
                    parameters_ultima_venta = (cliente_id,)
                    result_ultima_venta = db_connection.execute_query(query_ultima_venta, parameters_ultima_venta)

                    if result_ultima_venta:
                        venta = Venta(result_ultima_venta[0][0], result_ultima_venta[0][1], result_ultima_venta[0][2],
                                      result_ultima_venta[0][3], result_ultima_venta[0][4], result_ultima_venta[0][5])

                        print(f"Última venta del cliente con ID {cliente_id}:")
                        print(f"Venta ID: {venta.id}, ID Producto: {venta.id_producto}, Cantidad: {venta.cantidad}, "
                              f"Fecha Inicio Compra: {venta.fecha_inicio_compra}, Fecha Fin Compra: {venta.fecha_fin_compra}")
                    else:
                        print(f"No hay ventas para el cliente con ID {cliente_id}")

                except Exception as e:
                    logging.error(f"Error al obtener la última venta: {e}")
            elif opcion == '4':
                logging.info("Se ha seleccionado la opción 4")
                try:
                    cliente_id = input("Ingrese el ID del cliente: ")
                    query_primera_venta = "SELECT * FROM ventas WHERE id_cliente = %s ORDER BY fecha_inicio_compra ASC LIMIT 1;"
                    parameters_primera_venta = (cliente_id,)
                    result_primera_venta = db_connection.execute_query(query_primera_venta, parameters_primera_venta)

                    if result_primera_venta:
                        venta = Venta(result_primera_venta[0][0], result_primera_venta[0][1], result_primera_venta[0][2], result_primera_venta[0][3], result_primera_venta[0][4], result_primera_venta[0][5])

                        print(f"Primera venta del cliente con ID {cliente_id}:")
                        print(f"Venta ID: {venta.id}, ID Producto: {venta.id_producto}, Cantidad: {venta.cantidad}, "
                              f"Fecha Inicio Compra: {venta.fecha_inicio_compra}, Fecha Fin Compra: {venta.fecha_fin_compra}")
                    else:
                        print(f"No hay ventas para el cliente con ID {cliente_id}")

                except Exception as e:
                    logging.error(f"Error al obtener la primera venta: {e}")
            elif opcion == '5':
                logging.info("Se ha seleccionado la opción 5")
                try:
                    producto_id = input("Ingrese el ID del producto: ")
                    query_existencias = "SELECT cantidad FROM reposicion WHERE id_producto = %s;"
                    parameters_existencias = (producto_id,)
                    result_existencias = db_connection.execute_query(query_existencias, parameters_existencias)

                    if result_existencias:
                        existencias = result_existencias[0][0]
                        print(f"Cantidad disponible del producto con ID {producto_id}: {existencias}")
                    else:
                        print(f"No hay existencias registradas para el producto con ID {producto_id}")

                except Exception as e:
                    logging.error(f"Error al obtener las existencias del producto: {e}")
            elif opcion == '6':
                logging.info("Se ha seleccionado la opción 6")
                salir = True
                print("Saliendo del programa.")
            else:
                print("Opción no válida. Inténtelo de nuevo.")
                continue
    except Exception as e:
        logging.error(f"Error al conectar a la base de datos: {e}")
    finally:
        db_connection.disconnect()
        logging.info("Programa finalizado.")
