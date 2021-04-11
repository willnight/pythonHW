def main(argv):
    price_num = 0
    new_price = 0
    if len(argv) > 1:
        price_num = int(argv[1])
    if len(argv) > 2:
        new_price = int(argv[2])

    try:
        bakery = open('bakery.csv', 'r', encoding='utf-8')
        file_lines = bakery.readlines()
        if 0 < price_num < len(file_lines):
            file_lines[price_num-1] = f'{new_price}\n'

        bakery = open('bakery.csv', 'w', encoding='utf-8')
        bakery.writelines(file_lines)
        bakery.close()

    except Exception:
        pass


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
