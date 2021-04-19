# *(вместо 1) Написать регулярное выражение для парсинга файла логов
# web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# для получения информации вида:
# (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
# например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
#
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? - на всех
# Были ли особенные строки? - да, с другими ip адресами и разным кол-м букв
# Можно ли для них уточнить регулярное выражение? - да, удалось в 1 записать

import re


def get_log_data(f, num):
    res = []
    with open(f, 'r', encoding='utf-8') as f:
        for cc in range(0, num):
            res.append(f.readline().rstrip())
    return res


def log_parse(log):
    pattern = r'((\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|(\w{0,4}:\w{0,4}:\w{0,4}:\w{0,4}:\w{0,4}:\w{0,4})) - - \[(\d{2}\/[A-Za-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] \"(GET|POST|get|post|HEAD|head) (.+) ((HTTP|http)\/[1-2]\.[0-9]") (\d{3}) (\d+) (-|"([^"]+)") (["]([^"]+)["])'
    compiled_pattern = re.compile(pattern)
    res = compiled_pattern.findall(log)
    return res[0][0], res[0][1], res[0][3], res[0][4], res[0][7], res[0][8]


logs = get_log_data('C:\\PyProjects\\pythonHW\\Mitrofanova_Daria_dz_6\\nginx_logs.txt', 20)
for i, el in enumerate(logs):
    print(f'{log_parse(el)}')
