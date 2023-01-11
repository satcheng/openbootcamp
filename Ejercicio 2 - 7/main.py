import workTimeManage.isWeekend.isWeekendCalculation
import workTimeManage.isWorkTime.isWorkTimeCalculation
import workTimeManage.timeToDeparture.hoursAndMinutesToDepartureCalculation


def main():

    _startTime = 9
    _departureTime = 20

    i1 = workTimeManage.isWeekend.isWeekendCalculation.isWeekendCalculation()
    i2 = workTimeManage.isWorkTime.isWorkTimeCalculation.isWorkTimeCalculation(_startTime, _departureTime)
    i3 = workTimeManage.timeToDeparture.hoursAndMinutesToDepartureCalculation.hoursAndMinutesToDepartureCalculation(_departureTime)


    isWeekend = i1.isWeekendDay()
    hourOfTheDay = i2.timeToWorkByHours()
    hoursAndMinutesToLeave = i3.hoursAndMinutesToDeparture()

    if isWeekend == "is-weekend":
        print("Es fin de semana")

    elif hourOfTheDay == "prework":
        print("Todavía no has entrado a trabajar")

    elif hourOfTheDay == "worktime":

        if hoursAndMinutesToLeave[0] == 0:

            print("Estás trabajando. Te quedan", hoursAndMinutesToLeave[1], "min para salir.")

        elif hoursAndMinutesToLeave[0] == 1:

            print("Estás trabajando. Te queda", hoursAndMinutesToLeave[0], "hora y", hoursAndMinutesToLeave[1], "min para salir.")

        else:

            print("Estás trabajando. Te quedan", hoursAndMinutesToLeave[0], "horas y", hoursAndMinutesToLeave[1], "min para salir.")

    elif hourOfTheDay == "afterwork":
        print("Has salido de trabajar.")

    else:
        print("Algo raro pasó.")


if __name__ == "__main__":
    main()