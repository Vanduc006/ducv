from datetime import date
#
day1 = date.today()
day2 = date(2006, 8, 28)


diff = day1 - day2
print(diff.days, "days so far!")