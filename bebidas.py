
class bebidas():
    def __init__(self, mililitros, sabor, compannia, fecha_caducidad):
        self.mililitros = mililitros
        self.sabor = sabor
        self.compannia = compannia
        self.fecha_caducidad = fecha_caducidad
    def __str__(self):
        libro=f"""
Nombre: {self.compannia}\n
Mililitros: {self.mililitros}\n
Sabor: {self.sabor}\n
Caducidad: {self.fecha_caducidad}\n

"""
        
        return libro


