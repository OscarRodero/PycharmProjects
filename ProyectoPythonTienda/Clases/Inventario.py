from datetime import datetime
class Inventario:
    def __init__(self, id: str, id_producto: int, fecha_actualizacion: datetime, cantidad_existente: int, cantidad_entrante: int, cantidad_saliente: int, id_venta: str, id_reposicion: str):
        self.id = id
        self.id_producto = id_producto
        self.fecha_actualizacion = fecha_actualizacion
        self.cantidad_existente = cantidad_existente
        self.cantidad_entrante = cantidad_entrante
        self.cantidad_saliente = cantidad_saliente
        self.id_venta = id_venta
        self.id_reposicion = id_reposicion

    def __str__(self):
        return f"ID: {self.id}, ID Producto: {self.id_producto}, Fecha Actualización: {self.fecha_actualizacion}, Cantidad Existente: {self.cantidad_existente}, Cantidad Entrante: {self.cantidad_entrante}, Cantidad Saliente: {self.cantidad_saliente}, ID Venta: {self.id_venta}, ID Reposicion: {self.id_reposicion}"