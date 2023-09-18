import FP
import Persona
from Direccion import direccion

def inicioPrograma():
    direccion1 = direccion("calle manuela", 1, "Bilbao", "Cantabria")
    print(direccion1.numero, direccion1.calle, direccion1.ciudad, direccion1.provincia)
    return 0

inicioPrograma()