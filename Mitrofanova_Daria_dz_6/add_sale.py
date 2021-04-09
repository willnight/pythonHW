def main(argv):
    price = argv[1]
    try:
        with open('bakery.csv', 'a', encoding='utf-8') as f:
            f.write(price + '\n')
    except Exception:
        return None


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
