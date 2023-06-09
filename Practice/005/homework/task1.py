#  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def exp(a, b):
    if b > 0:
        b -= 1
        return exp(a, b) * a
    else:
        return 1

a = int(input('Введите основание(a): '))
b = int(input('Введите степень(b): '))
result = 0
print(f' {a} в степени {b} = {exp(a,b)}')