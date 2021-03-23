import json
# *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
# «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
# реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
# Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
#
# Как поступить, если потребуется сортировка по ключам? - sorted() или json.dumps с sort_keys=True


def thesaurus_adv(*args):
    result_dict = {}
    for el in args:
        first_letter_name = el[0]
        first_letter_surname = el.split(' ')[-1][0]
        if result_dict.get(first_letter_surname) is None:
            result_dict[first_letter_surname] = {first_letter_name: [el]}
        else:
            surname_dict = result_dict.get(first_letter_surname)
            if surname_dict.get(first_letter_name) is None:
                surname_dict[first_letter_name] = [el]
            else:
                surname_dict.get(first_letter_name).append(el)
    return result_dict


result = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(json.dumps(result, indent=4, sort_keys=True, ensure_ascii=False))
