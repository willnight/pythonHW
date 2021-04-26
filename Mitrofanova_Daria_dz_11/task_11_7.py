# Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число».
# Реализовать перегрузку методов сложения и умножения комплексных чисел. Проверить работу проекта.
# Для этого создать экземпляры класса (комплексные числа), выполнить сложение и
# умножение созданных экземпляров. Проверить корректность полученного результата.

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        try:
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        except TypeError:
            print("Введенные данные не корректны! Проверьте, что все аргументы числовые!")

    def __mul__(self, other):
        try:
            return ComplexNumber((self.real * other.real - self.imag * other.imag), (self.real * other.imag + self.imag * other.real))
        except TypeError:
            print("Введенные данные не корректны! Проверьте, что все аргументы числовые!")

    def __str__(self):
        return f"({self.real}{self.imag if self.imag < 0 else f'+{self.imag}'}j)"


complex_1 = ComplexNumber(-6, 0.1)
complex_2 = ComplexNumber(1, -2)
check_1 = complex(-6, 0.1)
check_2 = complex(1, -2)

print(complex_1)
print(complex_2)
print(f"Сумма: {complex_1 + complex_2}")
print(f"Произведение: {complex_1 * complex_2}")
print('-' * 30)
print(check_1)
print(check_2)
print(f"Сумма проверочная: {check_1 + check_2}")
print(f"Произведение проверочное: {check_1 * check_2}")
