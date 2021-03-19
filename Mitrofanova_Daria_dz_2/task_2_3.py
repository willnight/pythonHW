# *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.

var_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
list_len = len(var_list)

while i < list_len:
    el = var_list[i]
    el1 = el.replace("+", "").replace("-", "")
    if el1.isdigit():
        if el.__contains__("+"):
            var_list[i] = f'+{int(el1):02d}'
        elif el.__contains__("-"):
            var_list[i] = f'-{int(el1):02d}'
        else:
            var_list[i] = f'{int(el1):02d}'

        var_list.insert(i, '"')
        var_list.insert(i + 2, '"')

        i += 3
        list_len += 2

    else:
        i += 1

print(var_list)
print(' '.join(var_list))
