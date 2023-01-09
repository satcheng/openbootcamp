class Vehiculo():

    _Color = None
    _Ruedas = None
    _Puertas = None


class Coche(Vehiculo):

    _Velocidad = None
    _Cilindrada = None

    def Acelerar(self):

        self._Velocidad = True

    def Andando(self):

        if self._Velocidad:

            print("El coche está en marcha")

        else:

            print("El coche está parado")

v1= Coche()

v1.Andando()

v1.Acelerar()

v1.Andando()
