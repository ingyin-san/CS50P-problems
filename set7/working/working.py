"""a function called convert that expects a str in any of the 12-hour formats below and
returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00)"""

import re


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    matches = re.search(r"^(\d{1,2}(?::\d{2})?) (AM|PM) to (\d{1,2}(?::\d{2})?) (AM|PM)$", s)
    if matches:
        start_time, start_period, end_time, end_period = matches.groups()
        start = to_24_hour(start_time, start_period)
        end = to_24_hour(end_time, end_period)
        return f"{start} to {end}"
    else:
        raise ValueError


def to_24_hour(time, period):
    if ':' in time:
        hour, minute = time.split(':')
        hr = int(hour)
        min = int(minute)
    else:
        hr = int(time)
        min = 0

    if hr < 1 or hr > 12:       #check if hours are valid
        raise ValueError

    if min < 0 or min > 59:     #check if minutes are valid
        raise ValueError

    #convert to 24-hour clock according to AM or PM
    if period == "AM":
        if hr == 12:
            hr = 0
    else:
        if hr != 12:
            hr += 12

    return(f"{hr:02}:{min:02}")


if __name__ == "__main__":
    main()
