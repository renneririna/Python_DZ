'''
Счастливый билет
Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером.

Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех.

Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

Вам требуется написать программу, которая проверяет счастливость билета с номером n 
и выводит на экран yes или no.

Пример:
n = 385916 -> yes
n = 123456 -> no
'''

n = 123456

n1 = n // 100000
n2 = n // 10000 % 10
n3 = n // 1000 % 10
n4 = n // 100 % 10
n5 = n // 10 % 10
n6 = n % 10

if (n1 + n2 + n3) == (n4 + n5 + n6):
    print('yes')
else:
    print('no')