def main(argv):
    start_num = 0
    end_num = 0
    if len(argv) > 1:
        start_num = int(argv[1])
    if len(argv) > 2:
        end_num = int(argv[2])

    try:
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            csv_reader = reader(f)
            if start_num == 0:
                for row in csv_reader:
                    print(row[0])
            elif start_num > 0 and end_num == 0:
                for row in list(csv_reader)[start_num - 1::]:
                    print(row[0])
            elif start_num > 0 and end_num > 0:
                for row in list(csv_reader)[start_num - 1:end_num]:
                    print(row[0])
    except Exception:
        pass


if __name__ == '__main__':
    import sys
    from csv import reader

    exit(main(sys.argv))
