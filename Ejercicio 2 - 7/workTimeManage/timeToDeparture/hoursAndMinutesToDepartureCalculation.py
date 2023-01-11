import time


class hoursAndMinutesToDepartureCalculation:

    def __init__(timming, _departureTime):

        timming._localTime = time.localtime()
        timming._departureTime: int = _departureTime

    def hoursAndMinutesToDeparture(timming):

        timming._hoursToDeparture = (timming._departureTime - timming._localTime.tm_hour) - 1

        timming._minutesToDeparture = 60 - timming._localTime.tm_min

        if  timming._minutesToDeparture == 60:

            timming._hoursToDeparture = timming._hoursToDeparture + 1

            timming._minutesToDeparture = 0

            return timming._hoursToDeparture, timming._minutesToDeparture

        else:

            return timming._hoursToDeparture, timming._minutesToDeparture
