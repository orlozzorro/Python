# Даны два массива чисел. 
# Требуется вывести те элементы первого массива (в том порядке, 
# в каком они идут в первом массиве), которых нет во втором массиве.

import random

list_1 = [random.randint(1, 20) for _ in range(int(input('Введите размер 1 списка: ')))]
list_2 = [random.randint(1, 20) for _ in range(int(input('Введите размер 2 списка: ')))]

print(list_1)
print(list_2)

final_list = []

for item in list_1:
    if not item in list_2:
        final_list.append(item)

print(final_list)
