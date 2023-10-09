class Vehiculo:
    def __init__(self, marca, modelo, asientos):
        self.marca = marca
        self.modelo = modelo
        self.asientos = asientos

    def obtenerInformacion(self):
        print(f"Marca: {self.marca} Modelo: {self.modelo}, Asientos: {self.asientos}")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, asientos, caballos):
        super().__init__(marca,modelo,asientos)
        self.caballos = caballos
    def obtenerInformacion(self):
        print(f"Marca: {self.marca} Modelo: {self.modelo}, Asientos: {self.asientos}, Caballos: {self.caballos}")

class Bicicleta:
    def __init__(self, marca, modelo, asientos, tipo):
        super().__init__(marca, modelo, asientos)
        self.tipo = tipo


