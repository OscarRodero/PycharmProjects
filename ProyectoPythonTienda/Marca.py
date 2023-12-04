class Marca:
    def __init__(self, id, descripcion):
        self.id = id
        self.descripcion = descripcion

    def __str__(self):
        return f"ID: {self.id}, Descripción: {self.descripcion}"