# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу? - искать через регулярки, но не стоит
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# - да, не будет теряться точность
# Сильно ли усложняется код функции при этом? - нет decimal.Decimal()
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# - да, сравнивать все в одном регистре
# В качестве примера выведите курсы доллара и евро.

import requests
import xmltodict
import json
import decimal


def currency_rates(curr_key):
    try:
        r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        decoded_response = r.content.decode('windows-1251')
        response_json = json.loads(json.dumps(xmltodict.parse(decoded_response)))

        for el in response_json.get("ValCurs").get("Valute"):
            if el.get("CharCode").upper() == curr_key.upper():
                return decimal.Decimal(el.get("Value").replace(',', '.'))
    except Exception:
        return None


print(currency_rates("EUR"))
print(currency_rates("usd"))
print(currency_rates("аа"))
