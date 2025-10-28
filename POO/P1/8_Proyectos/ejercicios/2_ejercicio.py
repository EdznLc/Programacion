class Calculadora:
    def _init_(self,n1,n2):
        self._n1=n1
        self._n2=n2

    @property
    def n1(self):
        return self._n1
    
    @n1.setter
    def n1(self,n1):
        self._n1=n1
    
    @property
    def n2(self):
        return self._n2
    
    @n2.setter
    def n2(self,n2):
        self._n2=n2

    def sumar(self):
        return self._n1+self._n2
    
    def restar(self):
        return self._n1-self._n2
    
    def multiplicar(self):
        return self._n1*self._n2
    
    def dividir(self):
        return self._n1/self._n2

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
operacion=Calculadora(n1,n2)
print(f"{operacion.n1}+{operacion.n2}={operacion.sumar()}")
print(f"{operacion.n1}-{operacion.n2}={operacion.restar()}")
print(f"{operacion.n1}*{operacion.n2}={operacion.multiplicar()}")
print(f"{operacion.n1}/{operacion.n2}={operacion.dividir()}")