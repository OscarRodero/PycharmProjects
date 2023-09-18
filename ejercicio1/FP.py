class FP:
    def __init__(self, descripcion):
        self.Descripcion = descripcion
        self.Personas = []
    def agregar(self, persona):
        self.Personas.append(persona)