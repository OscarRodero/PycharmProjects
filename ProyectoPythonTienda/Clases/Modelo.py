class Modelo:
    def __init__(self, id: str, descripcion: str):
        self.id = id
        self.descripcion = descripcion

    def __str__(self):
        return f"ID: {self.id}, Descripción: {self.descripcion}"