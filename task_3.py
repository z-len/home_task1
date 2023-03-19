"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

num = int(input('Введите целое положительное число: '))
num_dec = num * 10 + num
num_sot = num * 100 + num * 10 + num
sum_total = num + num_dec + num_sot
print(f'{num} + {num_dec} + {num * 100 + num * 10 + num} = {sum_total}')
