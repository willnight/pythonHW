# Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
import re


def extract_data(text):
    return text.split(' ')[0], re.split('\"(.*?) ', text)[1], re.split('\"(.*?) ', text)[2].split(" ")[0]


def get_log_data(f):
    result_list = []
    with open(f, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            result_list.append(extract_data(line))

    return result_list


print(get_log_data('nginx_logs.txt'))
