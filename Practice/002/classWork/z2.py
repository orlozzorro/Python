# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# number = int(input('Введите число >'))
# fib_prev = 0
# fib_curr = 1
# n = 1
# while fib_curr < number:
#     fib_next = fib_prev + fib_curr
#     fib_prev = fib_curr
#     fib_curr = fib_next
#     n += 1
    
# if fib_curr == number:
#     print(n)
# else:
#     print(-1)

number = int(input('Введите число: '))

fibo_1, fibo_2, index = 0, 1, 1

while fibo_2 < number:
    fibo_1, fibo_2 = fibo_2, fibo_1 + fibo_2
    index += 1
if fibo_2 == number:
    print(index)
else:
    print(-1)