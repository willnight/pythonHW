# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы
# — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"


dict_numbers_translation = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(eng):
    if len(eng):
        if eng[0].isupper():
            return dict_numbers_translation.get(eng.lower()).capitalize()
        else:
            return dict_numbers_translation.get(eng)
    else:
        return None


print(num_translate_adv("one"))
print(num_translate_adv("Two"))
print(num_translate_adv("eleven"))
print(num_translate_adv(""))
