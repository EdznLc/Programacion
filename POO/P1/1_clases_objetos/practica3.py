class Alumnos:
    def __init__(self, nombre, edad, matricula):
        self.__nombre = nombre
        self.__edad = edad
        self.__matricula = matricula
    
    def inscribirse(self):
        return f"El alumno {self.__nombre} se ha inscrito"
    
    def estudiar(self):
        return f"El alumno {self.__nombre} esta estudiando"
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nuevo):
        self.__nombre = nuevo
    
    def getEdad(self):
        return self.__edad
    
    def setEdad(self, nuevo):
        self.__edad = nuevo
    
    def getMatricula(self):
        return self.__matricula
    
    def setMatricula(self, nuevo):
        self.__matricula = nuevo

class Cursos:
    def __init__(self, nombre, codigo, creditos):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__creditos = creditos
    
    def asignar(self):
        return f"Se asigno el curso de  {self.__nombre}"
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nuevo):
        self.__nombre = nuevo
    
    def getCodigo(self):
        return self.__codigo
    
    def setCodigo(self, nuevo):
        self.__codigo = nuevo
    
    def getCreditos(self):
        return self.__creditos
    
    def setCreditos(self, nuevo):
        self.__creditos = nuevo

class Profesores:
    def __init__(self, nombre, experiencia, num_profesor):
        self.__nombre = nombre
        self.__experiencia = experiencia
        self.__num_profesor =  num_profesor
    
    def impartir(self):
        return f"El profesor {self.__nombre} esta impartiendo un curso"
    
    def evaluar(self):
        return f"El profesor {self.__nombre} esta evaluando"
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nuevo):
        self.__nombre = nuevo
    
    def getExperiencia(self):
        return self.__experiencia
    
    def setExperiencia(self, nuevo):
        self.__experiencia = nuevo
    
    def getNum_Profesor(self):
        return self.__num_profesor
    
    def setNum_Profesor(self,nuevo):
        self.__num_profesor = nuevo

alumno1 = Alumnos("Jose Alberto",19,"3141240120")
alumno2 = Alumnos("Luis Hector",19,"3141240113")
print(alumno1.inscribirse())
print(alumno1.estudiar())


curso1 = Cursos("Programacion","1234",10)
curso2 = Cursos("Calculo Integral","1235",8)
print(curso1.asignar())


profesor1 = Profesores("Juan Omar",20,"123123123")
profesor2 = Profesores("Blanca Rubi",15,"321321321")
print(profesor1.impartir())
print(profesor1.evaluar())


