# Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведённых типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за
# приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).
# Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


from utils import f_path, isint
import json
from collections import namedtuple


def json_decoder(data):
    return namedtuple('X', data.keys())(*data.values())


def json2obj(data):
    return json.loads(data, object_hook=json_decoder)


with open(f"{f_path}city.json", 'r', encoding='utf-8') as f_obj:
    content = f_obj.read()
    city_data = dict(json2obj(content))

def dict_to_str(dict):
    return f'{", ".join([" - ".join([str(key), str(val)]) for key, val in dict.items()])}'


class Warehouse:
    totalItemsCount = 0
    items = []

    def __init__(self, capacity):
        self.capacity = int(capacity)

    def add_to_wh(self, cell):
        if self.free_cells > 0:
            self.items.append(cell)
            self.totalItemsCount += 1
        else:
            print("Вы не можете добавить позицию на склад, нет мест!")

    @property
    def get_dict(self):
        return {"capacity": self.capacity, "freeCells": self.free_cells, "totalCells": self.totalItemsCount, "cells": self.items}

    @property
    def wh_capacity(self):
        return self.capacity

    @property
    def free_cells(self):
        return self.capacity - self.totalItemsCount

    @property
    def get_items(self):
        return self.items


class Unit:
    def __init__(self, code):
        self.code = code
        self.city = city_data.get(self.code)

    @property
    def get_dict(self):
        return {"code": self.code, "city": self.city}


class Equipment:
    def __init__(self, size, color, weight, name, type, **kwargs):
        self.size = size
        self.color = color
        self.weight = weight
        self.name = name
        self.type = type

    @property
    def get_dict(self):
        return {"size": self.size, "color": self.color, "weight": self.weight, "name": self.name, "type": self.type}


class Printer(Equipment):
    def __init__(self, size, color, weight, name):
        super().__init__(size, color, weight, name, type='Принтер')


class Scanner(Equipment):
    def __init__(self, size, color, weight, name):
        super().__init__(size, color, weight, name, type='Сканнер')


class Xerox(Equipment):
    def __init__(self, size, color, weight, name, is_color):
        self.size = size
        self.color = color
        self.weight = weight
        self.name = name
        self.type = 'Ксерокс'
        self.is_color = is_color

    @property
    def get_dict(self):
        return {"size": self.size, "color": self.color, "weight": self.weight, "name": self.name, "type": self.type, "colored": self.is_color}


class Cell:
    id = 1

    def __init__(self, unit, equip):
        self.unit = unit
        self.equip = equip
        self.id = Cell.id
        Cell.id += 1

    @property
    def get_dict(self):
        return {"id": self.id, "unit": self.unit.get_dict, "equip": self.equip.get_dict}

    @staticmethod
    def move_to_unit(id, code):
        new_unit = Unit(code)
        for item in wh.items:
            if item.get('id') == id:
                item.update({'unit': new_unit.get_dict})
        print(f"Груз перемещен в {city_data.get(code)}!")


# для теста вручную
# item_1 = Printer('30cm', 'red', 34, 'Epson Printer')
# item_2 = Scanner('45cm', 'blue', 3, 'Epson scan')
# item_3 = Xerox('82cm', 'gray', 21, 'Xerox 300', is_color=True)
#
# cell_1 = Cell(Unit(78), item_2)
# cell_2 = Cell(Unit(77), item_3)
# cell_3 = Cell(Unit(92), item_1)
# wh = Warehouse(12)
# wh.add_to_wh(cell_1.get_dict)
# wh.add_to_wh(cell_2.get_dict)
# wh.add_to_wh(cell_3.get_dict)
# print(wh.items)
# Cell.move_to_unit(1, 77)
# Cell.move_to_unit(2, 10)
# print(wh.items)
# print(wh.get_dict)


my_list = list()
current_command = None
commands = ["move", "exit", "add", "+", "?", "all", "random", "save"]
types = ['1 - Принтер', '2 - Сканнер', '3 - Ксерокс']

print("Программа для демонстрации склада активирована!")

while True:
    cap = input("Введите кол-во мест на складе: ")
    if isint(cap):
        wh = Warehouse(cap)
        break
    else:
        print("Вы ввели не число!")
        continue

print("Для просмотра справки по командам - напиши '?'")


def add_ogr_item(type):

    name = input("Введите название оборудования (модель, номер): ")
    size = input("Ввведите размер Д*Ш*В: ")
    color = input("Цвет оборудования: ")
    try:
        weight = float(input("Вес в кг: "))
    except ValueError:
        try:
            weight = float(input("Вес не распознался, введите еще раз или ставим по-умолчанию! Вес в кг: "))
        except ValueError:
            weight = 0

    code = input(f"Отлично! В каком городе нужно хранить, введите код города\n{dict_to_str(city_data)}: ")
    if isint(code):
        unit = Unit(code)
    else:
        unit = Unit(78)

    if type == "1":
        printer = Printer(size, color, weight, name)
        wh.add_to_wh(Cell(unit, printer).get_dict)
        print(f"Груз отправлен в {city_data.get(code)}")
    elif type == "2":
        scan = Scanner(size, color, weight, name)
        wh.add_to_wh(Cell(unit, scan).get_dict)
        print(f"Груз отправлен в {city_data.get(code)}")
    elif type == "3":
        is_col = input("Это цветной ксерокс? Введите 'y' / 'n' : ")
        is_col = True if is_col.lower() == 'y' else False
        xerox = Xerox(size, color, weight, name, is_col)
        wh.add_to_wh(Cell(unit, xerox).get_dict)
        print(f"Груз отправлен в {city_data.get(code)}")


while True:
    command = current_command
    if current_command is None:
        command = input("Введите команду: ")

    if command == "?":
        print("для выхода 'exit'")
        print("для перемещения в другой город 'move'")
        print("для добавления элемента 'add' или '+'")
        print("для просмотра всех элементов 'all'")
        print("для рандомного добавления значений 'random'")
        print("для сохранения файла в json файл 'save'")
        current_command = None
        continue

    if command == "exit":
        current_command = None
        break

    if command == "save":
        with open(f"warehouse.json", "w", encoding='utf-8') as write_f:
            json.dump(wh.get_dict, write_f, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
        current_command = None
        continue

    if command == "move":
        print("Для перемещения груза в другой город введите его id и новый код города: ")
        for el in wh.items:
            print(el)
        id = int(input("Id груза: "))
        code = int(input(f"Код города {city_data}: "))
        Cell.move_to_unit(id, code)
        current_command = None
        continue

    if command == "random":
        item_1 = Printer('30cm', 'red', 34, 'Epson Printer')
        cell_1 = Cell(Unit(78), item_1)
        wh.add_to_wh(cell_1.get_dict)
        continue

    if command == "all":
        for el in wh.items:
            print(el)
        current_command = None
        continue

    if command not in commands:
        print("Вы ввели что-то не то :( Или я не понял")
        current_command = None
        continue

    if command == "add" or command == "+":
        if wh.free_cells > 0:
            while True:
                text = input(f"Введите тип оборудования: {', '.join(types)}: ")

                if text in ('1', '2', '3'):
                    add_ogr_item(text)
                    break

                elif text in commands:
                    current_command = text
                    break

                else:
                    print("Вы ввели что-то не то :( Или я не понял")

            continue
        else:
            print("Вы не можете добавить позицию на склад, нет мест!")
            continue

