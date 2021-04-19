# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
#
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# нужно учитывать символы в адресе - _ .
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re


def email_parse(email_address):
    pattern = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,4}$'
    compiled_pattern = re.compile(pattern)
    res = re.match(compiled_pattern, email_address)
    if res is None:
        raise ValueError(f'wrong email: {email_address}')
    else:
        pattern_parse = r'(?P<username>[^&]+)@(?P<domain>[^&]+)[.]'
        compiled_pattern = re.compile(pattern_parse)
        res_dict = map(lambda x: x.groupdict(), compiled_pattern.finditer(email_address))
        # print(*res_dict, sep=', ')
        return res_dict


emails = ['ivanpetrov@mail.ru', 'ivan-Petrov@gmail.com', 'Ivan.Petrov@yandex.ru', 'Ivan_Petrov@test.info',
          'ivanpetrovmail.ru', 'ivan-Petrov@gmailcom', 'Ivan.Petrofdyandex.ru', '!!!Ivan_Petrov@test.info']

for el in emails:
    print(email_parse(el))
