from datetime import datetime

class Producto:
    def __init__(self, id: str, descripcion: str, precio: float, id_marca_modelo: str, fecha_creacion: datetime):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.id_marca_modelo = id_marca_modelo
        self.fecha_creacion = fecha_creacion

    def __str__(self):
        return f"ID: {self.id}, Descripción: {self.descripcion}, Precio: {self.precio}, ID MarcaModelo: {self.id_marca_modelo}, Fecha Creación: {self.fecha_creacion}"