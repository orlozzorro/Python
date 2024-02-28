# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
import random

MAX_VALUE = 5
MIN_VALUE = 0
COUNT_ELEMENTS = 20

my_list = [random.randint(-10, 10) for _ in range(COUNT_ELEMENTS)]
indexes_list = list()
print(my_list)
for i in range(len(my_list)):
    if MIN_VALUE < my_list[i] < MAX_VALUE:
        indexes_list.append(i)

print(indexes_list)