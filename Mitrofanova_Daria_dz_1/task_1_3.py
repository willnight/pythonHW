# Реализовать склонение слова «процент» для чисел до 20.
# Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
# Вывести все склонения для проверки.

input_strings_for_test = ["1", "2", "5", "11", "15", "21", "22", "25", "1001", "10111", "102"]
for input_string in input_strings_for_test:
    input_num = int(input_string)

    sec_string = 'процент'
    sec_string_ending = 'ов'

    input_string_len = len(input_string)
    last_digit = int(input_string[input_string_len - 1])
    two_last_digits = last_digit

    if input_string_len >= 2:
        two_last_digits = int(input_string[input_string_len - 2] + input_string[input_string_len - 1])

    if last_digit == 1:
        sec_string_ending = ''

    if last_digit in range(2, 5):
        sec_string_ending = 'а'

    if 14 >= two_last_digits >= 11:
        sec_string_ending = 'ов'

    print(input_string + ' ' + sec_string + sec_string_ending)
