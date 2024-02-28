# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

input_sentence = "пара-ра-рам рам-пам-папам па-ра-па-да"
phrases = list()
phrases = input_sentence.split()
vowels = 'уеыаоэяию'
count_vowels = list()
for item in phrases:
    c_vowels = 0
    char_items = list(item)
    for char in char_items:
        if char in vowels:
            c_vowels += 1
    count_vowels.append(c_vowels) 

if len(set(count_vowels)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")