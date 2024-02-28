# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15



def ar_progress(start_value, step, count):
    my_list = list()
    my_list.append(start_value)
    next_value = start_value
    while count > 1:
        next_value += step
        my_list.append(next_value)
        count -=1
    return my_list

start_value = int(input('Введите начальное значение: '))
step = int(input('Введите шаг: '))
count = int(input('Введите количество элементов: '))

print(ar_progress(start_value, step, count))