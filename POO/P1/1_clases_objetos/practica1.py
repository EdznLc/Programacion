
def area_rectangulo(base, altura):
    return base * altura

print(f"EL area es: {area_rectangulo(2,4)}")

class Rectangulo:
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    

rectangulo1 = Rectangulo(2, 3)
print(f"El area del rectangulo 1 es: {rectangulo1.area()}")