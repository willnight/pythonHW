# *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#     {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
#
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

import os
import json

root_path = 'C:\\Users\\dmitr\\Downloads'
nums_list = [10 ** n for n in range(1, 10)]
result_dict = {}
for el in nums_list:
    result_dict[el] = [0, set()]

if os.path.exists(root_path):
    for file in os.listdir(root_path):
        file_size = os.stat(os.path.join(root_path, file)).st_size
        file_ext = os.path.splitext(file)[1].replace('.', '')
        for i in range(1, len(nums_list)):
            if nums_list[i - 1] <= file_size < nums_list[i]:
                result_dict[nums_list[i]][0] = result_dict.get(nums_list[i])[0] + 1
                if file_ext != '':
                    result_dict[nums_list[i]][1].add(file_ext)

for k, v in result_dict. items():
    result_dict[k] = (v[0], list(v[1]))

with open('file_stats.json', 'w', encoding='utf-8') as outfile:
    outfile.write(json.dumps(result_dict, indent=4, sort_keys=True, ensure_ascii=False))
