# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
# и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
#
# Примечание: сможете ли вы замаскировать работу декоратора? @wraps
from functools import wraps


def val_checker(my_func):
    def _val_checker(func):
        @wraps(func)
        def val_checker_wrapper(*args, **kwargs):
            custom_val = args[0]
            if my_func(custom_val):
                return func(custom_val)
            else:
                raise ValueError(f'wrong val {custom_val}')
        return val_checker_wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(4))
print(calc_cube(-4))
