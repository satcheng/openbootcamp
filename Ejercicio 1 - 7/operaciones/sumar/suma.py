class sumarDosVariables:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def sumatorioDosNumeros(self):
        resultado = self._x + self._y
        return int(resultado)
