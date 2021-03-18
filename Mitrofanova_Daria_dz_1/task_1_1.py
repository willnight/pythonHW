# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

input_seconds = 455977

seconds_in_day = 86400
seconds_in_hour = 3600
# input_seconds = int(input("Введите секунды: "))
# print(input_seconds, 'сек')
if input_seconds >= 0:
    days = input_seconds // seconds_in_day
    hours = input_seconds % seconds_in_day // seconds_in_hour
    minutes = input_seconds % seconds_in_day % seconds_in_hour // 60
    seconds = input_seconds % seconds_in_day % seconds_in_hour % 60

    time_values = [days, hours, minutes, seconds]
    time_values_suffix = [" дн ", " ч ", " мин ", " сек "]

    time_string = ''
    for i, el in enumerate(time_values):
        if el != 0:
            time_string += str(el) + time_values_suffix[i]

    print(time_string)
else:
    print("Вы ввели отрицательную длительность!")
