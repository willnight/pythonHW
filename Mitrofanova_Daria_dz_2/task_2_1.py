# 1. Выяснить тип результата выражений:
# 15 * 3 - int
# 15 / 3 - float
# 15 // 2 - int
# 15 ** 2 - int

var_list = ['15 * 2', '15 / 3', '15 // 2', '15 ** 2']

for i in var_list:
    print(f"тип выражения '{i}' - {type(eval(i))}")