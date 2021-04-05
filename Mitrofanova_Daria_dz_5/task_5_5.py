# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
#
#
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

from collections import Counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# в лоб
src_distinct = [el for el in src if src.count(el) == 1]

# небольшая оптимизация
unique_list = list(Counter(src))
unique_distinct = [el for el in unique_list if src.count(el) == 1]

print(src)
print(src_distinct)
print(unique_list)
print(unique_distinct)
