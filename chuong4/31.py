def days_in_month(month, year):
    if month == 2:
        # Check if it's a leap year
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
month = 2
year = 2022
days = days_in_month(month, year)
print(f"There are {days} days in month {month} of year {year}.")  

