from datetime import datetime, timedelta

def parse_time(time_str):
    return datetime.strptime(time_str, "%H:%M")

def time_difference(time1_str, time2_str):
    t1 = parse_time(time1_str)
    t2 = parse_time(time2_str)

    # If t2 is less than t1, then we suppose it's next day
    if t2 < t1:
        t2 += timedelta(days=1)

    diff = t2 - t1
    total_seconds = int(diff.total_seconds())

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60

    return hours, minutes


if __name__ == "__main__":
    print("Time difference Calc")
    time1 = input("Enter Time 1 (HH:MM): ")
    time2 = input("Enter Time 2 (HH:MM): ")

    h, m = time_difference(time1, time2)

    print(f"\nBetween {time1} and {time2}:")
    print(f"{h} hour(s), {m} minute(s)")
