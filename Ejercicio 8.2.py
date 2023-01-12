import pickle

class Vehicule:

    _name = ""
    _model = ""

    def __init__(self, _name, _model):
        self._name = _name
        self._model = _model

    def getName(self):
        return self._name


j1 = Vehicule("Opel", "Corsa")

f = open("datos1.bin", "wb")

pickle.dump(j1, f)

f.close()

g = open("datos1.bin", "rb")

car = pickle.load(g)

print(type(car))
print(car.getName())
