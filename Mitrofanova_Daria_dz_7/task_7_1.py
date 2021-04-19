# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
#
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); - проверять на существование
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# - json или yaml
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
# - да

import os


def check_folder_exist(root, name):
    return os.path.exists(os.path.join(root, name))


root_path = 'C:\PyProjects\pythonHW\Mitrofanova_Daria_dz_7'
main_folder = 'my_project'
project_folders = ['settings', 'mainapp', 'adminapp', 'authapp']

if not check_folder_exist(root_path, main_folder):
    os.mkdir(main_folder)

for folder in project_folders:
    if not check_folder_exist(os.path.join(root_path, main_folder), folder):
        os.mkdir(os.path.join(root_path, main_folder, folder))
