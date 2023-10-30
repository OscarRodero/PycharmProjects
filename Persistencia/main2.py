class Producto:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    def descuento(self, descuento):
        self.precio = self.precio*((100-descuento)/100)

class Laptop(Producto):
    def __init__(self, marca, modelo, precio, procesador, memoria):
        super().__init__(marca, modelo, precio)
        self.procesador = procesador
        self.memoria = memoria

class Tablet(Producto):
    def __init__(self, marca, modelo, precio, pulgadas):
        super().__init__(marca, modelo, precio)
        self.pulgadas = pulgadas
    def descuento(self, descuento):
        self.precio = self.precio*((100-descuento)/100)
        self.precio = self.precio*0.9

np = Producto("HP","ASF34",200)
np.descuento(25)
print(np.precio)

np2 = Tablet("DQ", "1234A", 120, 3.5)
np2.descuento(15)
print(np2.precio)