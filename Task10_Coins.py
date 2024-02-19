"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

Пример:
5 -> 1 0 1 1 0
2
"""

n = int(input('Введите количество монет '))
orel = reshka = 0
for i in range(n):
    m = int(input('Орёл(1) или Решка(0): '))
    if m == 1:
        orel += 1
    else:
        reshka += 1
if orel < reshka:
    print(f'Необходимо перевернуть {orel} монет с "орёл" на "решка", их меньше всего')
elif orel == reshka:
    print(f'Количество монет "орёл" и "решка" одинаково, по {orel} шт.')
else:
    print((f'Необходимо перевернуть {reshka} монет с "решка" на "орёл", их меньше всего'))