# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.


def list_sum(l_1, l_2):
    return [x + y for x, y in zip(l_1, l_2)]


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        res = ''
        for x in self.matrix:
            for y in x:
                res += f"{y : ^10}"
            res += '\n'
        return res

    def __add__(self, other):
        res = []
        try:
            for i, x in enumerate(self.matrix):
                res.append(list_sum(x, other.matrix[i]))
        except IndexError:
            return Matrix(res)
        return Matrix(res)


m_1 = Matrix([[31, 22, 2], [54, 6, 9], [8, 5, -1]])
m_2 = Matrix([[11, 5, -1], [4, 26, 4], [-4, 66, 45], [1, 4, 5]])
print(m_1)
print("-" * 30)
print(m_2)
print("-" * 30)
print("Сумма матриц:")
print(m_1 + m_2)
