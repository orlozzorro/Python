# 1. Открыть файл
# 2. Сохранить файл
# 3. Посмотреть все контакты
# 4. Создать контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход


# phone_book = []
# def show_contacts():
#     file = open('sample.txt', 'r', encoding='UTF-8')
#     data = file.readlines()
#     file.close()
#     print(data)


# show_contacts()




# for contact in data:
#     new_contact = contact.strip().split(';')
#     new_contact = {'name':new_contact[0],
#                    'phone':new_contact[1],
#                    'comment':new_contact[2]}
#         phone_book.append(new_contact)

# phone_book.append({'name': 'Антон Пальчиков',
#                    'phone': '999-999',
#                    'comment': 'Друг Ноггано'})
# print(phone_book)

# new_phone_book = []
# for contact in phone_book:
#     new_contact = ';'.join([values for values in contact.values()])
#     new_phone_book.append(new_contact)

# new_phone_book = '\n'.join(new_phone_book)

# file = open('sample.txt', 'w', encoding='UTF-8')
# file.write(new_phone_book)
# file.close()

# cont = '\nАнгелина Воробьева;4564654;Куртизанка'

# file = open('sample.txt', 'a', encoding='UTF-8')
# file.write(cont)
# file.close()

# with open('sample.txt', 'a', encoding='UTF-8') as file:
#     file.write(cont)



def add_cont():
    file = open('sample.txt', 'a', encoding='UTF-8')
    data1 = input('введите ФИО: ')
    data2 = input('номер телефона: ')
    data3 = input('место работы: ')
    data = '\n' + data1 + '; ' + data2 + '; ' + data3  
    print(data)
    file.write(data)
    file.close()

def read_cont():
    file = open('sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for contact in data:
        print(contact)
# read_cont()

def find_cont():
    file = open('sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    search_cont = input('введите для поиска информацию: ')
    for cont in data:
        if search_cont.lower() in cont.lower():
            print(cont)
# find_cont()

def change_cont():
    phone_book = []

    file = open('sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    i = 0
    for contact in data:
        new_contact = contact.strip().split(';')
        new_contact = {'id': i,
                    'name':new_contact[0],
                    'phone':new_contact[1],
                    'comment':new_contact[2]}
        phone_book.append(new_contact)
        i +=1
    print(phone_book)
    elem = int(input('введите id: '))
    print(phone_book[elem])
    
change_cont()
