class Venta:
    def __init__(self, id, id_producto, cantidad, id_cliente, fecha_inicio_compra, fecha_fin_compra):
        self.id = id
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.id_cliente = id_cliente
        self.fecha_inicio_compra = fecha_inicio_compra
        self.fecha_fin_compra = fecha_fin_compra

    def __str__(self):
        return f"ID: {self.id}, ID Producto: {self.id_producto}, Cantidad: {self.cantidad}, ID Cliente: {self.id_cliente}, Fecha Inicio Compra: {self.fecha_inicio_compra}, Fecha Fin Compra: {self.fecha_fin_compra}"