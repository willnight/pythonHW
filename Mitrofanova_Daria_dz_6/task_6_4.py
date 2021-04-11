# *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Только теперь не нужно создавать словарь с данными. Вместо этого нужно сохранить объединенные
# данные в новый файл (users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи
#

hobbies = open('hobby.csv', 'r', encoding='utf-8')
users_hobby = open('users_hobby.txt', 'a', encoding='utf-8')

with open('users.csv', 'r', encoding='utf-8') as users:
    for line in users.readlines():
        hobbies_str = hobbies.readline().strip()
        if hobbies_str != '':
            users_hobby.write(f'{line.strip()}: {hobbies_str}\n')
        else:
            users_hobby.write(f'{line.strip()}: {None}\n')

hobbies.close()
users_hobby.close()
