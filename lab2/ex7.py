day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400)

def day_of_year(day,month,year):
    day_of_year = 0
    if is_leap(year):
        day_in_month[2] += 1
    else:
        if month == 2 and day == 29:
            return -1
    for i in range(1,month):
        print(day_in_month[i])
        day_of_year += day_in_month[i]
    day_of_year += day
    
    return day_of_year    

print(day_of_year(2,3,2023))