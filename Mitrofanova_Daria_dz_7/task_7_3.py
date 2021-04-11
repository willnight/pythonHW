# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
#
#
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
# это реальная задача, которая решена, например, во фреймворке django.

import os
import shutil

root_project_path = 'my_project'
template_folder = 'templates'


def html_files_filter(src_list):
    return list(filter(lambda x: x.__contains__('.html'), src_list))


if os.path.exists(root_project_path):
    for root, dirs, files in os.walk(root_project_path):
        html_files = html_files_filter(files)
        if len(files) > 0 and len(html_files) > 0:
            directory_name = root.split('\\')[-1]

            if not os.path.exists(os.path.join(root_project_path, template_folder)):
                os.mkdir(os.path.join(root_project_path, template_folder))

            if not os.path.exists(os.path.join(root_project_path, template_folder, directory_name)):
                os.mkdir(os.path.join(root_project_path, template_folder, directory_name))

                for file in html_files:
                    shutil.copy2(os.path.join(root, file),
                                 os.path.join(root_project_path, template_folder, directory_name, file))
