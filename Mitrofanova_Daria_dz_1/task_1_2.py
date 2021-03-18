# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

num = 1000
num_add = 17
num_list = []
sum_7 = 0
sum_7_17 = 0
need_print = False

for i in range(num):
    if i % 2 == 1:
        num_list.append(i ** 3)

print(num_list)
print('-' * 10)

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7
for i in num_list:
    if need_print: print('el', i)
    digits_sum = 0

    for index, el in enumerate(str(i)):
        digits_sum += int(el)
    if need_print: print('d sum', digits_sum)

    if digits_sum % 7 == 0:
        sum_7 += i
    if need_print: print('-' * 10)

# К каждому элементу списка добавить 17 и заново вычислить сумму
for i in num_list:
    item = i + num_add
    if need_print: print('el', i + num_add)
    digits_sum = 0

    for index, el in enumerate(str(item)):
        digits_sum += int(el)
    if need_print: print('d sum', digits_sum)

    if digits_sum % 7 == 0:
        sum_7_17 += item
    if need_print: print('*' * 10)

print('result a: ' + str(sum_7))
print('result b: ' + str(sum_7_17))
