# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

input_seconds = 400153
# input_seconds = int(input("Введите секунды: "))
# print(input_seconds, 'сек')
if input_seconds >= 0:
    days = input_seconds // (60 * 60 * 24)
    hours = (input_seconds // 3600) - (24 * days)
    minutes = (input_seconds // 60) - (60 * hours) - (days * 24 * 60)
    seconds = input_seconds - ((hours * 3600) + (minutes * 60) + (days * 24 * 60 * 60))

    time_values = [days, hours, minutes, seconds]
    time_values_suffix = [" дн ", " ч ", " мин ", " сек "]

    time_string = ''
    for i, el in enumerate(time_values):
        if el != 0:
            time_string += str(el) + time_values_suffix[i]

    print(time_string)
else:
    print("Вы ввели отрицательную длительность!")
