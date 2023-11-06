import os, shutil
mi_lista = ["var","log", "resultado1", "resultado2", "11062023", "recuperacion.txt", "archivo.log"]
def contar_palabras(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return len(archivo.read().split())


if not os.path.exists(mi_lista[0]):
    os.makedirs(mi_lista[0])
if not os.path.exists(mi_lista[1]):
    os.makedirs(mi_lista[1])
os.chdir(mi_lista[0])
if not os.path.exists(mi_lista[2]):
    os.makedirs(mi_lista[2])
if not os.path.exists(mi_lista[3]):
    os.makedirs(mi_lista[3])
os.chdir(mi_lista[2])
with open(mi_lista[5], "w") as archivo:
    archivo.write("Recuperación del sistema base")
os.chdir("../../"+mi_lista[1])
if not os.path.exists(mi_lista[4]):
    os.makedirs(mi_lista[4])
os.chdir(mi_lista[4])
with open(mi_lista[6], "w") as archivo:
    archivo.write("Archivo log de nuestro sistema")
os.chdir("../../"+mi_lista[0]+"/"+mi_lista[2])
shutil.copy(mi_lista[5], "../"+mi_lista[3]+"/resultado2.txt")
os.chdir("../../"+mi_lista[1]+"/"+mi_lista[4])
shutil.move(mi_lista[6],"../../"+mi_lista[0]+"/"+mi_lista[3]+"/"+mi_lista[6])
palabras1 = contar_palabras("../../"+mi_lista[0]+"/"+mi_lista[2]+"/"+mi_lista[5])
palabras2 = contar_palabras("../../"+mi_lista[0]+"/"+mi_lista[3]+"/"+mi_lista[6])
print(palabras1)
print(palabras2)
