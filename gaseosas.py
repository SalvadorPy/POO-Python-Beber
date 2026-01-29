from bebidas import bebidas

class gaseosas(bebidas):
    def __init__(self,  mililitros, sabor, compannia, fecha_caducidad, cantidad_sellos):

        super().__init__( mililitros, sabor, compannia, fecha_caducidad)
        self.cantidad_sellos = cantidad_sellos


