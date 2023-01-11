import time


class isWeekendCalculation:

    def __init__(self):

        self._horaLocal = time.localtime()
        self._startWeekend = 6
        self._isWeekend = "is-not-weekend"

    def isWeekendDay(self):

        if self._horaLocal.tm_wday >= self._startWeekend:

            self._isWeekend = "is-weekend"

            return self._isWeekend

        else:

            return self._isWeekend
