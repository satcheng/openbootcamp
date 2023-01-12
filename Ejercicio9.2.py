from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]


resultado = filter(lambda x: x % 2 != 0, numeros)
sumado = reduce(lambda x, y: x+y, resultado)

print(sumado)
