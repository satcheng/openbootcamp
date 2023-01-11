import operaciones.sumar.suma
import operaciones.restar.resta
import operaciones.multiplicar.multiplica
import operaciones.dividir.divide

def main():
    i1 = operaciones.sumar.suma.sumarDosVariables(2, 2)
    i2 = operaciones.restar.resta.restaDosVariables(2, 2)
    i3 = operaciones.multiplicar.multiplica.multiplicaDosVariables(2, 2)
    i4 = operaciones.dividir.divide.divideDosVariables(2, 2)

    print(i1.sumatorioDosNumeros())
    print(i2.restaDosNumeros())
    print(i3.multiplicaDosNumeros())
    print(i4.divideDosNumeros())

if __name__ == "__main__":
    main()
