"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.

Пример:
4 4 -> 2 2 
5 6 -> 2 3
"""

S = int(input('Задайте 1-ю подсказку (сумму двух чисел от 1 до 1000): '))
P = int(input('Задайте 2-ю подсказку (произведение двух чисел от 1 до 1000): '))
if S < 1 or S > 1000 or P < 1 or P > 1000:
    print('Вы ввели числа не из заданного диапазона!')
for x in range(S):
    for y in range(P):
        if S == x + y and P == x * y:
            print(f'Первое загаданное число = {x}, Второе загаданное число = {y}')
