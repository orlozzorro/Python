# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

cranes = int(input('Введите количество  журавликов > '))
Petya_and_Seregha_cranes = int(cranes / 3)
Katya_cranes = int(Petya_and_Seregha_cranes * 2)
if (Katya_cranes + Petya_and_Seregha_cranes == cranes):
    print(f'Катя сделала {Katya_cranes} журавлика(-ов)')
    print(f'Петя и Сережа сделали по {int(Petya_and_Seregha_cranes/2)} журавлика(-ов)')
else:
    print("Ребята не доделали работу. Напишите, сколько получилось, после того, как они доделали работу")

