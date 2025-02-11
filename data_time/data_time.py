from datetime import date, time, datetime

date_now = date.today()

print(date_now)


date_format = date.fromisoformat("2025-10-24")

print(date_format)

print(date_format.strftime("%A, %B %d, %Y"))

today = datetime.today()

print(today)
