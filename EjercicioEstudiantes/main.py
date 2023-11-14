import os
from Estudiante import Estudiante
def insertarEstudiante():
    try:
        nombre = input("Dame un nombre")
        apellidos = input("Dame los apellidos")
        edad = input("Dame la fecha de nacimiento")
        calificacion = input("Dame la calificación")
        estudiante = Estudiante(nombre, apellidos, edad, calificacion)
        with open("venv/Estudiantes/"+estudiante.nombre + "_" + estudiante.apellidos + ".txt", "w") as a:
            mi_texto = nombre+","+apellidos+","+edad+","+calificacion
            texto = mi_texto.replace(" ", "")
            a.write(texto)
    except Exception:
        print("Error al insertar el estudiante.")

def GuardarYSalir():
    try:
        archivos = os.listdir("venv/Estudiantes")
        contador = 0
        with open("script.txt", "w") as script:
            for archivo in archivos:
                contador+=1
                with open("venv/Estudiantes/"+archivo, "r") as arch:
                    info = arch.readline().strip()
                    nombre, apellidos, edad, calificacion = info.split(",")
                    inserts = f"INSERT INTO Estudiantes VALUES ('{contador}','{nombre}', '{apellidos}', '{edad}', '{calificacion}');\n"
                    script.write(inserts)
    except FileNotFoundError:
        print("El archivo no existe")
    except Exception:
        print("Error al guardar")


def imprimirMenu():
    print("Bienvenido, ¿qué desea hacer?")
    print("1.- Insertar Estudiante")
    print("2.- Guardar y Salir")
    print("Cualquier otra cosa para salir.")
    x = input()
    if(x=="1"):
        insertarEstudiante()
        return False
    elif(x=="2"):
        GuardarYSalir()
        return True
    else:
        return True

def abrirMenu():
    salir = False
    while not salir:
        salir = imprimirMenu()

abrirMenu()