days = ['mon','tues','wed','thurs','fri','sat','sun']
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
leapYear = 0

dayOfWeek = 'mon'
day = 1
month = 'jan'
year = 1900

def getNextDay(dayOfWeek, month, day, year):
    if month == 'dec' and day == 31:
        year += 1
    if year % 4 == 0:
        if year == 1900:
            leapYear = 0
        else:
            leapYear = 1
    else:
        leapYear = 0
    for position, item in enumerate(days):
        if item == dayOfWeek:
            if item == 'sun':
                dayOfWeek = 'mon'
            else:
                dayOfWeek = days[position + 1]
            break
    if month == 'jan' or month == 'mar' or month == 'may' or month == 'jul' or month == 'aug' or month == 'oct' or month == 'dec':
        if day == 31:
            day = 1
            for position, item in enumerate(months):
                if item == month:
                    if item == 'dec':
                        month = 'jan'
                    else:
                        month = months[position + 1]
                    break
        else:
            day += 1
    elif month == 'apr' or month == 'jun' or month == 'sep' or month == 'nov':
        if day == 30:
            day = 1
            for position, item in enumerate(months):
                if item == month:
                    month = months[position + 1]
                    break
        else:
            day += 1
    elif month == 'feb':
        if leapYear == 1:
            if day == 29:
                day = 1
                month = 'mar'
            else:
                day += 1
        elif leapYear == 0:
            if day == 28:
                day = 1
                month = 'mar'
            else:
                day += 1
    return dayOfWeek, month, day, year

a = 0
while 1 + 1 == 2:
    if day == 1 and dayOfWeek == 'sun':
        if year != 1900:
            a += 1
    dayOfWeek, month, day, year = getNextDay(dayOfWeek, month, day, year)
    if day == 31 and month == 'dec' and year == 2000:
        break
print a
