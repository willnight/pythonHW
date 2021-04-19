# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
#
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? - да func.__name__
# Сможете ли решить задачу для именованных аргументов? - да
# Сможете ли вы замаскировать работу декоратора? - да
# Сможете ли вывести имя функции, например, в виде: - да
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

def type_logger(func):
    args_list = []

    def type_logger_wrapper(*args, **kwargs):
        nonlocal args_list
        args_list.extend(list(map(lambda x: f'{x}: {type(x)}', args)))
        args_list.extend(list(map(lambda x: f'{x}({kwargs.get(x)}): {type(kwargs.get(x))}', kwargs.keys())))
        res = ', '.join(args_list)
        print(f'{func.__name__}({res})')
        logger = func(*args, **kwargs)
        return logger
    return type_logger_wrapper


@type_logger
def calc_cube(x, y, z, test='gg', ps=4):
    return x ** 3


calc_cube(4, '656', [5, 6], test='gg', ps=4)
