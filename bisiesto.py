import time

class extractCaracteristicsOfYears():

    def isLeapYear(year):

        if type(year) is not int:

            print("Error 1: El año debe ser tipo entero.")

        elif year < 1900:

            print("Error 2: El año debe ser mayor que 1900.")

        elif year > 2200:

            print("Error 3: El año debe ser menor que 2200.")

        else:

            defineYear = (year, 12, 31, 0, 0, 0, 0, 0, 0)

            descomposedYearAttributes = time.localtime(time.mktime(defineYear))

            if descomposedYearAttributes.tm_yday == 366:

                print("Es año bisiesto.")

            else:

                print("No es año bisiesto.")

yearToAnalyse = int(input("Introduce el año que quieras saber: "))

extractCaracteristicsOfYears.isLeapYear(yearToAnalyse)
