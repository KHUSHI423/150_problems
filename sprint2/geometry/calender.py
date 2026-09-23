day, month, year = map(int, input().split())

# January and February
if month == 1:
    month = 13
    year -= 1
elif month == 2:
    month = 14
    year -= 1

q = day
K = year % 100
J = year // 100

h = (q + (13 * (month + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7

days = [
    "Saturday",
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

print(days[h])