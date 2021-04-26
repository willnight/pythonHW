# Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверить его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

import utils


class MyZeroDivision(Exception):
    def __init__(self, text):
        self.text = text


v_1 = 0
v_2 = 0

v_1_flag = True
v_2_flag = True

while True:
    if v_1_flag:
        val_1 = input("Введите делимое: ")
        if not utils.isfloat(val_1):
            print("Вы ввели не число!")
            continue
        else:
            v_1_flag = False
            v_1 = float(val_1)

    if v_2_flag:
        val_2 = input("Введите делитель: ")
        if not utils.isfloat(val_2):
            print("Вы ввели не число!")
            continue
        else:
            v_2_flag = False
            v_2 = float(val_2)

    if not (v_1_flag and v_2_flag):
        break

try:
    if v_2 == 0:
        raise MyZeroDivision("Вы хотите делить на ноль! Так не получится")
except MyZeroDivision as err:
    print(err)
else:
    print(f"{round(v_1 / v_2, 2)}")
