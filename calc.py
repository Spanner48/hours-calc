from datetime import datetime, timedelta

def parse_time(time_str):
    return datetime.strptime(time_str, "%H:%M")

def time_difference(time1_str, time2_str):
    t1 = parse_time(time1_str)
    t2 = parse_time(time2_str)

    # Если второе время меньше первого — считаем, что это следующий день
    if t2 < t1:
        t2 += timedelta(days=1)

    diff = t2 - t1
    total_seconds = int(diff.total_seconds())

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60

    return hours, minutes


if __name__ == "__main__":
    print("Калькулятор разницы времени")
    time1 = input("Введите Время 1 (HH:MM): ")
    time2 = input("Введите Время 2 (HH:MM): ")

    h, m = time_difference(time1, time2)

    print(f"\nМежду {time1} и {time2}:")
    print(f"{h} час(ов), {m} минут")
