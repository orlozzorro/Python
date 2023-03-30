# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.

from random import randint
def circ(a, mn, mx):
    return a % mx+mn

N = 7
arr = [randint(1, 15) for e in range(N)]
print(arr)
counts = 0
for e in range(len(arr)):
    if arr[circ(e-1, 0, N)] < arr[e] > arr[circ(e+1, 0, N)]:
        counts += 1
        # print(e)
print(counts)
