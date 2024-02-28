import random

rand_list= [random.randint(0,100) for _ in range(15)]
print(rand_list)
# ============================
# for i, item in enumerate(rand_list, 1):
#     print(i, item)
# ===================================

letter_list = list('ghjhfdsajgklhg')
print(letter_list)
new_list = list(zip(rand_list, letter_list))
print(new_list)