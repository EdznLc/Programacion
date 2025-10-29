class Subject:
    def __init__(self):
        self._observers = []

    def agregar_observador(self, observer):
        self._observers.append(observer)

    def notificar(self):
        for observer in self._observers:
            observer.actualizar()

class Observer:
    def actualizar(self):
        pass

class ConcreteObserver(Observer):
    def actualizar(self):
        print("¡Nueva noticia publicada!")

# Uso del patrón Observer
noticias = Subject()
usuario1 = ConcreteObserver()
usuario2 = ConcreteObserver()

noticias.agregar_observador(usuario1)
noticias.agregar_observador(usuario2)

noticias.notificar()  # Imprime: ¡Nueva noticia publicada! (dos veces)
