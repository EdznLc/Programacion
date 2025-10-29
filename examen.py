class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def get_llantas(self):
        return self._llantas
    
    def get_color(self):
        return self._color
    
    def get_precio(self):
        return self._precio
    
    def set_llantas(self, llantas):
        self._llantas = llantas
    
    def set_color(self, color):
        self._color = color
    
    def set_precio(self, precio):
        self._precio = precio

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas,color,precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas,color,precio)

vehiculo = Fabrica(4, "Rojo", 1500)
moto = Moto(2, "Azul", 2000)
carro = Carro(4, "Gris", 3000)


print(vehiculo.get_color(), vehiculo.get_llantas(), vehiculo.get_precio())
print(moto.get_color(), moto.get_llantas(), moto.get_precio())
print(carro.get_color(), carro.get_llantas(), carro.get_precio())
