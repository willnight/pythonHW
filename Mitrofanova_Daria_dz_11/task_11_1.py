# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый — с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, data):
        self.data = data

    @classmethod
    def get_num_values(cls, data):
        res = list(map(lambda x: int(x), data.split("-")))
        if Date.validate_num(res):
            return cls(data)
        else:
            return None

    @staticmethod
    def validate_num(obj):
        res = True
        if obj[1] not in range(1, 13):
            print(f"Вы ввели некорректные данные! Месяц должен быть в пределах от 1 до 12! Вы ввели {obj[1]}")
            res = False
        return res

    def __str__(self):
        if self is not None:
            return f"Дата: {'-'.join(list(map(lambda x: f'0{x}' if int(x) in range(1, 10) and len(x) == 1 else x, self.data.split('-'))))}"


date_1 = Date.get_num_values("25-11-2020")
print(date_1)
print()
date_2 = Date.get_num_values("25-15-2020")
print(date_2)
print()
date_3 = Date.get_num_values("25-09-2020")
print(date_3)
print()
date_4 = Date.get_num_values("25-8-2020")
print(date_4)
