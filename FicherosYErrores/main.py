import tkinter as tk
from tkinter import filedialog

def sumar_numeros_archivo():
    root = tk.Tk()
    root.withdraw()

    while True:
        archivos_seleccionados = filedialog.askopenfilenames(
            title="Seleccionar archivo(s)",
            filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")),
            multiple=True
        )

        if not archivos_seleccionados:
            print("No se seleccionó ningún archivo.")
            break

        for nombre_archivo in archivos_seleccionados:
            try:
                with open(nombre_archivo, 'r') as archivo:
                    suma_total = 0
                    for linea in archivo:
                        try:
                            numero = int(linea)
                            suma_total += numero
                        except ValueError:
                            print(f"Error: La línea '{linea.strip()}' no contiene un número entero válido en el archivo '{nombre_archivo}'.")
                    print(f"\nSuma total del archivo '{nombre_archivo}': {suma_total}\n")
            except FileNotFoundError:
                print(f"Error: El archivo '{nombre_archivo}' no existe. Por favor, ingrese un nombre de archivo válido.")
            except Exception as e:
                print(f"Error inesperado al leer el archivo '{nombre_archivo}': {e}")
        break
sumar_numeros_archivo()
