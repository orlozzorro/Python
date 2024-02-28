# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no
def sum(digit):
    sum = digit // 100 + digit % 100 // 10 + digit % 10
    return sum

ticket = int(input('Введите 6-значный номер билета > '))
digit_1 = ticket // 1000
digit_2 = ticket % 1000


if (sum(digit_1) == sum(digit_2)):
    print(f'{ticket} -> yes')
else: 
    print(f'{ticket} -> no')
 