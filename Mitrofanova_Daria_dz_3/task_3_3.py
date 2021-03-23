import json
# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
#
# Подумайте: полезен ли будет вам оператор распаковки?
# Как поступить, если потребуется сортировка по ключам? - можно использовать вывод через json.dumps с sort_keys=True
# либо итерироваться в функции for el in sorted(args)
# Можно ли использовать словарь в этом случае?


def thesaurus(*args):
    result_dict = {}
    for el in args:
        first_letter = el[0]
        if result_dict.get(first_letter) is None:
            result_dict[first_letter] = [el]
        else:
            result_dict.get(first_letter).append(el)
    return result_dict


result = thesaurus("Иван", "Мария", "Петр", "Илья")
print(json.dumps(result, indent=4, sort_keys=True, ensure_ascii=False))
