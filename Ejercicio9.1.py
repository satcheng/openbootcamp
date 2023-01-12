countries = {"Argentina", "France", "Italy", "Spain", "Argentina"}

countriesSorted = sorted(countries)

mensaje: str = ""

i = 0

for n in countriesSorted:


    if i < int(len(countriesSorted)-2):

        mensaje += n
        mensaje += ", "

    elif i == int(len(countriesSorted)-2):

        mensaje += n
        mensaje += " and "

    else:
        mensaje += n
        mensaje += "."

    i += 1
