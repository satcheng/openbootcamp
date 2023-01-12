countries = {"Argentina", "France", "Italy", "Spain", "Argentina"}

countriesSorted = sorted(countries)

message: str = ""

i = 0

for n in countriesSorted:


    if i < int(len(countriesSorted)-2):

        message += n
        message += ", "

    elif i == int(len(countriesSorted)-2):

        message += n
        message += " and "

    else:
        message += n
        message += "."

    i += 1

print(message)

