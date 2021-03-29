# * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
# - dict, можно парсить дату через datetime.datetime.strptime(date_str, '%d.%m.%Y')

import requests
import xmltodict
import json
import decimal
import datetime


def currency_rates(curr_key):
    try:
        r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        decoded_response = r.content.decode('windows-1251')
        response_json = json.loads(json.dumps(xmltodict.parse(decoded_response)))

        date_str = response_json.get("ValCurs").get("@Date")
        date_time_obj = datetime.datetime.strptime(date_str, '%d.%m.%Y')

        for el in response_json.get("ValCurs").get("Valute"):
            if el.get("CharCode").upper() == curr_key.upper():
                currency_value = decimal.Decimal(el.get("Value").replace(',', '.'))
                return {"date": date_time_obj.date(), "value": currency_value}

    except Exception:
        return None


print(currency_rates("EUR"))
print(currency_rates("usd"))
print(currency_rates("usd").get("date"))
print(currency_rates("usd").get("value"))
print(currency_rates("аа"))
