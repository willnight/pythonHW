# *(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:

import requests
import xmltodict
import json
import decimal
import datetime


def main(argv):
    curr_key = argv[1]
    try:
        r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        decoded_response = r.content.decode('windows-1251')
        response_json = json.loads(json.dumps(xmltodict.parse(decoded_response)))

        date_str = response_json.get("ValCurs").get("@Date")
        date_time_obj = datetime.datetime.strptime(date_str, '%d.%m.%Y')

        for el in response_json.get("ValCurs").get("Valute"):
            if el.get("CharCode").upper() == curr_key.upper():
                currency_value = decimal.Decimal(el.get("Value").replace(',', '.'))
                return print({"date": date_time_obj.date(), "value": currency_value})

    except Exception:
        return None


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
