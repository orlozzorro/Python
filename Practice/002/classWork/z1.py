# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 
# 0! = 1 Решить задачу используя цикл while

number = abs(int(input('Введите число >')))

factorial = 1
while number > 1:
    factorial *= number
    number -= 1
print(factorial)