# *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
#
#
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
# (не программно);
# предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.


import yaml
import os


def check_folder_exist(root, name):
    return os.path.isdir(os.path.join(root, name))


def check_file_exist(root, name):
    return os.path.isfile(os.path.join(root, name))


def create_file(path, name):
    if not os.path.exists(os.path.join(path, name)):
        f = open(os.path.join(path, name), 'w', encoding='utf-8')
        f.close()


with open('config.yaml', encoding='utf-8') as config:
    config_yaml = yaml.load(config, Loader=yaml.FullLoader)

    for k, v in config_yaml.items():
        file_path = ''
        if not check_folder_exist(file_path, k):
            os.mkdir(k)
        if not check_file_exist(file_path, k):
            create_file(file_path, k)

        for k2, v2 in v.items():
            file_path = k
            if isinstance(v2, dict):
                if not check_folder_exist(file_path, k2):
                    os.mkdir(os.path.join(file_path, k2))

                for k3, v3 in v2.items():
                    file_path = os.path.join(k, k2)
                    if isinstance(v3, dict):
                        if not check_folder_exist(file_path, k3):
                            os.mkdir(os.path.join(file_path, k3))

                        for k4, v4 in v3.items():
                            file_path = os.path.join(k, k2, k3)
                            if isinstance(v4, dict):
                                if not check_folder_exist(file_path, k4):
                                    os.mkdir(os.path.join(file_path, k4))

                                for k5, v5 in v4.items():
                                    file_path = os.path.join(k, k2, k3, k4)
                                    if isinstance(v5, dict):
                                        if not check_folder_exist(file_path, k5):
                                            os.mkdir(os.path.join(file_path, k5))
                                    else:
                                        if not check_file_exist(file_path, k5):
                                            create_file(file_path, k5)
                            else:
                                if not check_file_exist(file_path, k4):
                                    create_file(file_path, k4)
                    else:
                        if not check_file_exist(file_path, k3):
                            create_file(file_path, k3)
            else:
                if not check_file_exist(file_path, k2):
                    create_file(file_path, k2)
