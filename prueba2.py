class Universidad:
    def __init__(self, nombreesc):
        self._nombreesc = nombreesc

    def get_nombre_esc(self):
        return self._nombreesc

    def set_nombre_esc(self, nombreesc):
        self._nombreesc = nombreesc

class Carrera(Universidad):
    def __init__(self, especialidad, nombreesc):
        super().__init__(nombreesc)
        self._especialidad = especialidad

    def get_especialidad(self):
        return self._especialidad

    def set_especialidad(self, especialidad):
        self._especialidad = especialidad

class Alumno(Carrera):
    def __init__(self, nombre, edad, especialidad, nombreesc):
        super().__init__(especialidad, nombreesc)
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

persona = Alumno("Edson", 19, "TI", "UTD")

print(persona.get_nombre(), persona.get_edad(), persona.get_especialidad(), persona.get_nombre_esc())