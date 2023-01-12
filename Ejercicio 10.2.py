
j1 = Tk()
e1 = StringVar()
listbox = Listbox(j1)

lista = ["Uno", "Dos", "Tres", "Cuatro"]

for item in lista:
    listbox.insert(END, item)

listbox.pack()

j1.mainloop()
