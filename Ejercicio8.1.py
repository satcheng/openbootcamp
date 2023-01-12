def main():

    def crearArchivo():
        f = open("archivoParaElEjercicio.txt", "w")

    def añadirAlFinal():
        f = open("hola.txt", "a")
        f.write("Contenido nuevo.\n")

    crearArchivo()

    añadirAlFinal()


if __name__ == "__main__":
    main()
