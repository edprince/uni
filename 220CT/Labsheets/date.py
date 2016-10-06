def calculateLeapYear(year):
    if (((year % 4 == 0) and (year % 100 != 0)) or year % 400 == 0):
        return True
def calculateDays(d, m, y):
    dates = {
        1:31,
        2:30,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
        }
    days = 0
    for i in range(1,m):
        days = days + dates[i]

    days += d
    if (calculateLeapYear(y) and m >= 2):
        days -= 2

    print('day number: ', days, ' - days left until ', y + 1, ': ', 365 - days)

day = int(input('enter a date: '))
month = int(input('enter a month: '))
year = int(input('enter a  year:' ))

calculateDays(day, month, year)
