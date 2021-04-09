# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

from collections import Counter


def get_log_data(f):
    result_list = []
    with open(f, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            result_list.append(line.split(' ')[0])

    return result_list


ip_list = get_log_data('nginx_logs.txt')
ordered_ip_dict = {k: v for k, v in sorted(Counter(ip_list).items(), key=lambda item: item[1], reverse=True)}
first_ip = next(iter(ordered_ip_dict))
print(f'спамер с ip {first_ip} сделал запросов {ordered_ip_dict.get(first_ip)}' )
