
def sum_del(p):
    summa = 0
    for e in range(1, p // 2 + 1):
        if p % e == 0:
            summa += e
    return summa

k = 10000
for n in range (1, k):
    m = sum_del(n)
    if n < m <= k and n == sum_del(m):
        print(n, m)
#---------------------------------------
def deviders(number: int) -> int:
    list_dev = []
    for div in range(1, number//2 + 1):
        if not number % div:
            list_dev.append(div)
    return sum(list_dev)


unique_list = []
for num in range(10000):
    if deviders(deviders(num)) == num and num != deviders(num):
        if not ((num, deviders(num))) in unique_list:
            unique_list.append((deviders(num), num))
            print(num, deviders(num))

# ----------------------------------

def func(i):
    num2=0
    for e in range(1,i):
        if i%e==0:
            num2+=e
    return num2

num=int(input('Введите число: '))
for i in range(num+1):
    var = func(i)
    var1 = func(var)
    if var == var1:
        print("++-------++")
        print("|",i,"-",var,"|")
        print("|---------|")
        print("|",var,"-",var1,"|")
        print("++-------++")
