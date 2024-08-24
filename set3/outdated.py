"""prompts the user for a date, anno Domini, in month-day-year order,
and output that same date in YYYY-MM-DD format."""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()

        if '/' in date:
            month, day, year = date.split('/')
        elif ',' in date:
            month_name, day, year = date.split(' ')
            day = day.rstrip(',')
            month = months.index(month_name) + 1
        else:
            continue

        day = int(day)
        month = int(month)
        year = int(year)
        if not (1 <= day <= 31 and 1 <= month <= 12 and 1000 <= year <= 9999):
            continue

        print(f"{year}-{month:02}-{day:02}")
        break
    except ValueError:
        pass
