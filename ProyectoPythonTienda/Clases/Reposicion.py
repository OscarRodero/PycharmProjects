from datetime import datetime


class Reposicion:
    def __init__(self, id: str, producto: str, cantidad: int, fecha_inicio_reposicion: datetime, fecha_fin_reposicion: datetime):
        self.id = id
        self.producto = producto
        self.cantidad = cantidad
        self.fecha_inicio_reposicion = fecha_inicio_reposicion
        self.fecha_fin_reposicion = fecha_fin_reposicion

    def __str__(self):
        return f"ID: {self.id}, Producto: {self.producto}, Cantidad: {self.cantidad}, Fecha Inicio Reposición: {self.fecha_inicio_reposicion}, Fecha Fin Reposición: {self.fecha_fin_reposicion}"