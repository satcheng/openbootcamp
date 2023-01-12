from tkinter import *

def choose():
    toShow.config(text="{}".format(opcion.get()))

def reset():
    opcion.set(None)
    toShow.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)
Radiobutton(root, text="Telecaster", variable=opcion,
            value='Telecaster', command=choose).pack(anchor=W)
Radiobutton(root, text="Stratocaster", variable=opcion,
            value='Stratocaster', command=choose).pack(anchor=W)
Radiobutton(root, text="Les Paul", variable=opcion,
            value='Les Paul', command=choose).pack(anchor=W)


toShow = Label(root)
toShow.pack()
Button(root, text="Restart", command=reset).pack()

root.mainloop()
