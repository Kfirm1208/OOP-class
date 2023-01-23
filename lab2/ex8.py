day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
def is_leap(year): 
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) 

def day_of_year(day,month,year):  
    day_of_years = 0 
    if is_leap(year): 
        day_in_month[2] += 1 
    else : 
        if month == 2 and day == 29 : 
            return -1 
    for i in range(1,month): 
        day_of_years += day_in_month[i]
    day_of_years += day 
    day_in_month[2] = 28 # reset
    return day_of_years

def date_diff(date1, date2):  
    days = 0 
    first_day = date1.split("-")  
    last_day = date2.split("-") 
    diff_year = int(last_day[2]) - int(first_day[2])
    DAY_1_FROMFIST = day_of_year(int(first_day[0]),int(first_day[1]),int(first_day[2]))  
    DAY_2_FROMFIST = day_of_year(int(last_day[0]),int(last_day[1]),int(last_day[2])) 
    if diff_year == 0 : 
        days = DAY_2_FROMFIST - DAY_1_FROMFIST
    if diff_year > 0 : 
        if is_leap(int(first_day[2])) : 
            days +=  (366 - DAY_1_FROMFIST)
        else : 
            days +=  (365 - DAY_1_FROMFIST )
        days += DAY_2_FROMFIST
        for i in range(diff_year - 1): 
            if is_leap(int(first_day[2])+1+i) : 
                days += 366 
            else : 
                days += 365

    return days +1

def day_in_year(year):
  days = 0
  if is_leap(year):
    days += 366
  else:
    days += 365
  return days
