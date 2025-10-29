# HERENCIA
class Personaje:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

class Guerrero(Personaje):  # Hereda de Personaje
    def __init__(self, nombre, nivel, fuerza):
        super().__init__(nombre, nivel)
        self.fuerza = fuerza

    def atacar(self):
        print(f"{self.nombre} ataca con fuerza {self.fuerza}!")

# COMPOSICIÓN
class Arma:
    def __init__(self, nombre, daño):
        self.nombre = nombre
        self.daño = daño

class Inventario:
    def __init__(self):
        self.arma = None  # Contendrá un objeto Arma

    def equipar(self, arma):
        self.arma = arma

# USO
espada = Arma("Espada legendaria", 50)
guerrero = Guerrero("Arthas", 10, 80)
inventario = Inventario()
inventario.equipar(espada)

# Mostrar resultado
print(f"{guerrero.nombre} - Nivel {guerrero.nivel}")
print(f"Arma equipada: {inventario.arma.nombre} (Daño {inventario.arma.daño})")
guerrero.atacar()