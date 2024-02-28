# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore 
import string

my_text = '''She sells sea shells on the sea shore The shells
        that she sells are sea shells I\'m sure. So if she sells sea
        shells on the sea shore I\'m sure that the shells are sea
        shore'''
# my_list = my_text.replace('.', '').lower()
# my_list = my_list.split()
# print(set(my_list))
# print(len(set(my_list)))
print(my_text)
punct = list(string.punctuation) + ['\n' + '\t']

for char in punct:
    my_text = my_text.replace(char, ' ')
print(my_text)
my_text = my_text.lower().split()
print(my_text)
print(len(set(my_text)))
dict_count = {}
for key in my_text:
    dict_count[key] = dict_count.get(key, 0) + 1
print(*dict_count.items(), sep = '\n')