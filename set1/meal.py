#prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.

def main():
    time = input("What time is it? ").strip().lower()
    if time.endswith(" a.m."):
        hour = convert(time.rstrip(" a.m."))
        if hour == 12:
            hour = 0
    elif time.endswith(" p.m."):
        hour = convert(time.rstrip(" p.m."))
        if hour != 12:
            hour += 12
    else:
        hour = convert(time)

    if 7 <= hour and hour <= 8:
        print("breakfast time")
    elif 12 <= hour and hour <= 13:
        print("lunch time")
    elif 18 <= hour and hour <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return (hours + minutes/60)


if __name__ == "__main__":
    main()
