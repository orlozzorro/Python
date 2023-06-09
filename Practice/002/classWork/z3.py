# Иван Васильевич пришел на рынок и решил купить два арбуза: 
# один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, 
# а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? 
# Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

from random import randint

print(randint(1000, 30000))

n = int(input('Введите количество арбузов: '))
max, min = 0, 30000

while n!=0:
    weight = randint(1000, 30000)
    print(weight)
    if weight > max:
        max = weight
    if weight < min:
        min = weight
    n -= 1
print(f'min={min}, max = {max}') 