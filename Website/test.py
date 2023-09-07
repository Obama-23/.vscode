import calendar
import time

print("Is the year a leap year or not?")
time.sleep(4)

class UserYear():
    def __init__(self, year: int):
        print(f"year proposed by user: {year}")
        self.year = year

# Create instances of UserYear class
YearNum1 = UserYear(2015)
YearNum2 = UserYear(2000)
YearNum3 = UserYear(2007)
YearNum4 = UserYear(2023)

print("the year you provided is...")
time.sleep(1.5)

# Check if each year is a leap year
years_to_check = [YearNum1.year, YearNum2.year, YearNum3.year, YearNum4.year]
for year in years_to_check:
    if calendar.isleap(year):
        print(f"{year} is a leap year!")
    else:
        print(f"{year} is not a leap year :(")
        # and that's it for today :P
        # yep
