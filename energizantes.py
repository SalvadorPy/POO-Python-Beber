from bebidas import  bebidas

class energizantes(bebidas):
    def __init__(self, mililitros, sabor, compannia, fecha_caducidad, cantidad_cafeina):
        super().__init__(mililitros, sabor, compannia, fecha_caducidad)
        self.cantidad_cafeina = cantidad_cafeina

