# import math
# машина проезжает за день M километров. За сколько дней она проедет N километров. If использовать нельзя

distance_per_day = int(input('сколько машина проедет за день > '))
distance = int(input('дистанция >'))
# math.ceil() - округление в большую сторону
# math. ()
#int() - отбросить дробную часть
# print(math.ceil(distance / distance_per_day))
print(f' Машине потребуется {(distance + distance_per_day -1)//distance_per_day}')
