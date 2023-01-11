class restaDosVariables:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def restaDosNumeros(self):
        resultado = self._x - self._y
        return int(resultado)
