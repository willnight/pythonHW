# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    """класс Road

    length : int
        длина дороги в метрах
    width : int
        ширина дороги в метрах
    thickness : int необязательное
        толщина полотна в см
    """

    def __init__(self, length, width, thickness=None):
        if type(length) == int and type(width) == int:
            self.__length = length
            self.__width = width
            if thickness is not None:
                self.thickness = thickness
            else:
                self.thickness = 1

    def road_mass(self):
        try:
            return int(self.__length * self.__width * 25 * self.thickness / 1000)
        except AttributeError:
            print(f"Длина и ширина должны быть числовыми значениями!")


road = Road(20, 5000, 5)
print(f"Для асфальтирования дороги нужно {road.road_mass()}т асфальта")
road2 = Road(20, 5000)
print(f"Для асфальтирования дороги нужно {road2.road_mass()}т асфальта")
road3 = Road(21, 50)
print(f"Для асфальтирования дороги нужно {road3.road_mass()}т асфальта")
