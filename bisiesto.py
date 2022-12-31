import time

class años():

    def bisiesto(year):

        t = (year, 12, 31, 0, 0, 0, 0, 0, 0)
        secs = time.mktime( t )

        e = time.localtime(secs)

        if e.tm_yday == 366:
            print("Es año bisiesto")
        else:
            print("No es año bisiesto")

años.bisiesto(2011)
