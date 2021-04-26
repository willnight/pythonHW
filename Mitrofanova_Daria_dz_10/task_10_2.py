# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @property
    @abstractmethod
    def tissue_consumption(self):
        pass

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption


class Coat(Clothes):

    @property
    def tissue_consumption(self):
        return round((self.size / 6.5) + 0.5)


class Jacket(Clothes):

    @property
    def tissue_consumption(self):
        return round((self.size * 2) + 0.3) / 100


cloth = Clothes
coat = Coat(8)
print(f"{coat.tissue_consumption}м ткани")
print("-" * 30)
jacket = Jacket(165)
print(f"{jacket.tissue_consumption}м ткани")
print("-" * 30)
print(f"{coat + jacket}м ткани")
