class Cliente:
    def __init__(self, id: str, nombre: str, cif: str, direccion: str):
        self.id = id
        self.nombre = nombre
        self.cif = cif
        self.direccion = direccion

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, CIF: {self.cif}, Dirección: {self.direccion}"