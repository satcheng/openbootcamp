import time


class isWorkTimeCalculation:

    def __init__(timming, _entryTime, _departureTime):

        timming._localTime = time.localtime()
        timming._timeStatus = None

        timming._entryTime: int = _entryTime
        timming._departureTime: int = _departureTime


    def timeToWorkByHours(timming):

        if timming._localTime.tm_hour < timming._entryTime:

            timming._timeStatus = "prework"

            return timming._timeStatus

        elif (timming._localTime.tm_hour >= timming._entryTime) and (timming._localTime.tm_hour < timming._departureTime):

            timming._timeStatus = "worktime"

            return timming._timeStatus

        else:

            timming._timeStatus = "afterwork"

            return timming._timeStatus
