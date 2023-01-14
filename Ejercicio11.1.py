import sqlite3 as sql


def crearDB():
    conn = sql.connect('colegio.sqlite')
    conn.commit()
    conn.close()

def crearTabla():
    conn = sql.connect('colegio.sqlite')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE alumnos (numAlumno integer, name TEXT, surname TEXT)")
    conn.commit()
    conn.close()

def insertarFila(numAlumno, name, surname):
    conn = sql.connect('colegio.sqlite')
    cursor = conn.cursor()
    instruccion = f'INSERT INTO alumnos VALUES ("{numAlumno}", "{name}", "{surname}")'
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def verTabla(_numAlumno):
    conn = sql.connect('colegio.sqlite')
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM alumnos WHERE numAlumno = '{_numAlumno}'"
    rows = cursor.execute(instruccion)

    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":

    crearDB()
    crearTabla()
    insertarFila(1, "Pepe", "Botika")
    insertarFila(2, "Paco", "Mer")
    insertarFila(3, "Sara", "Toga")
    insertarFila(4, "Ana", "Cleto")
    insertarFila(5, "Fran", "Quicia")
    insertarFila(6, "Edu", "Cado")
    insertarFila(7, "Eva", "Siva")
    insertarFila(8, "Mar", "Mota")
    verTabla(4)
