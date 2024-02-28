# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером)
import random
my_list = [random.randint(0,10) for i in range(10)]
count = 0
print(my_list)
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i-1]:
        count +=1
print(count)