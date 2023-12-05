class MarcaModelo:
    def __init__(self, id:str , id_marca: str, id_modelo: str):
        self.id = id
        self.id_marca = id_marca
        self.id_modelo = id_modelo

    def __str__(self):
        return f"ID: {self.id}, ID Marca: {self.id_marca}, ID Modelo: {self.id_modelo}"