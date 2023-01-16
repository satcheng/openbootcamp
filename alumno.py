class Alumno():

    def __init__(self, Nombre, Nota):
        
        if Nota >= 5:

            print("El alumno", Nombre, "ha aprobado.")

        else:
        
             print("El alumno", Nombre, "ha suspendido.")

Alumno("Paco",9.5)
