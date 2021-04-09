# **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
# чтобы можно было задать имя обоих исходных файлов и имя выходного файла.
# Проверить работу скрипта

def main(argv):
    name_users = ''
    name_hobbies = ''
    name_user_hobbies = ''
    if len(argv) > 1:
        name_users = argv[1]
    if len(argv) > 2:
        name_hobbies = argv[2]
    if len(argv) > 3:
        name_user_hobbies = argv[3]

    try:
        hobbies = open(name_hobbies, 'r', encoding='utf-8')
        users_hobby = open(name_user_hobbies, 'a', encoding='utf-8')

        with open(name_users, 'r', encoding='utf-8') as users:
            for line in users.readlines():
                hobbies_str = hobbies.readline().strip()
                if hobbies_str != '':
                    users_hobby.write(f'{line.strip()}: {hobbies_str}\n')
                else:
                    users_hobby.write(f'{line.strip()}: {None}\n')

        hobbies.close()
        users_hobby.close()

    except Exception:
        print("Произошла ошибка! Проверьте правильность ввода названий!")
        pass


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
