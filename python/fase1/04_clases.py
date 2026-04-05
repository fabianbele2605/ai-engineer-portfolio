class Estudiante:
    def __init__(self, nombre, fase=1):
        self.nombre = nombre
        self.fase = fase
        self.temas = []

    def aprender(self, tema):
        self.temas.append(tema)
        print(f"{self.nombre} aprendió: {tema}")

    def estado(self):
        return f"Fase {self.fase}/6 | Temas: {len(self.temas)}"
    

fabian = Estudiante("Fabian")
fabian.aprender("variables")
fabian.aprender("funciones")
fabian.aprender("archivos")
fabian.aprender("clases")
print(fabian.estado())
