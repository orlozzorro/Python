import random
# Дан список чисел, определите сколько в нем встречается различных чисел
my_list = [random.randint(0,10) for i in range(20)]

# Тоже самое:
# my_list = []
# for i in range(20):
#     my_list.append(random.randint(0,10))

print(my_list)
print(set(my_list))
print(len(set(my_list)))