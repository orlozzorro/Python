# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#    1 2 3 4 5
#   3
#    -> 1

# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
count = int(input('Введите количество элементов в массиве: '))
number = int(input('Введите число: '))
result = 0
diff_base = -1

my_list = [random.randint(0,10) for i in range(count)]
near_value = my_list[0]

print(f'Сгенерирована коллекция: \n{my_list} \n Вы ввели число: {number}')

for i in range(len(my_list)):
    if my_list[i] == number:
        result +=1
    else:
        if my_list[i] > number:
            diff = my_list[i] - number
        else:
            diff = number - my_list[i]
        if diff_base == -1:
            diff_base = diff
        if diff <= diff_base:
            near_value = my_list[i]
            diff_base = diff

if result > 0:
    print(f'Ваше число встречается в коллекции {result} раз')
else:
    print(f'Вашего числа нет в коллеции, но ближайшее к Вашему числу -> {near_value}')
