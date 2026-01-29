from bebidas import bebidas


class hidratantes(bebidas):
    def __init__(self, mililitros, sabor, compannia, fecha_caducidad, cantidad_electrolitos):
        super().__init__(mililitros, sabor, compannia, fecha_caducidad)
        self.cantidad_electrolitos = cantidad_electrolitos
