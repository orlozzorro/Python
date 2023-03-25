# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.


# mass=[1,2,3,4,5,5,4,3,2]
# mn=min(mass)
# mx=max(mass)
# for e in range(len(mass)):
#     if mass[e]==mx:
#         mass[e]=mn
# print(mass)


import random

list_1 = list()
n = int(input('Введите число элементов в списке: '))
n = range(n)
count = 0
for i in n: 
    i = random.randint(1,10)
    list_1.append(i)
print(list_1)
min_1 = list_1[0]
max_1 = list_1[0]
for i in range(len(list_1)):
    if min_1 > list_1[i]:
        min_1 = list_1[i]
    if max_1 < list_1[i]:
        max_1 = list_1[i]
print(f'{min_1} and {max_1}')
for i in range(len(list_1)):
    if max_1 == list_1[i]:
        list_1[i] = min_1
print (list_1)
