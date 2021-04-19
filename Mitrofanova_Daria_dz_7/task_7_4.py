# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи —
# верхняя граница размера файла (пусть будет кратна 10), а значения —
# общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
#
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat

import os

root_path = 'C:\\Users\\dmitr\\Downloads'
nums_list = [10 ** n for n in range(1, 8)]
result_dict = {}
for el in nums_list:
    result_dict[el] = 0

if os.path.exists(root_path):
    for file in os.listdir(root_path):
        file_size = os.stat(os.path.join(root_path, file)).st_size
        for i in range(1, len(nums_list)):
            if nums_list[i - 1] <= file_size < nums_list[i]:
                result_dict[nums_list[i]] = result_dict.get(nums_list[i]) + 1

print(result_dict)
