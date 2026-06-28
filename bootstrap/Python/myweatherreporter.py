import datetime
import calendar
city = input("Enter your city: ")
temperature = int(input("Enter today's temperature (c): "))
print("\nWeather Report")
print("city:",city)
if temperature >= 35:
    print("Weather: Very Hot")
elif temperature >= 25:
    print("Weather: Pleasant")
elif temperature >= 15:
    print("Weather: Cool")
else:
    print("Weather: Cold")

now = datetime.datetime.now()
print("\nToday's date:",now.date())
print("Current Time:",now.time())
print("\nCalendar for Current Year")
print(calendar.calendar(now.year))

