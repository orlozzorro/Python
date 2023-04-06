# 1. Открыть файл
# 2. Сохранить файл
# 3. Посмотреть все контакты
# 4. Создать контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход


def open_file():
    path_phone_book = input('Укажите путь к файлу: ')
    print(f'All OK. You use {path_phone_book}')
    return path_phone_book

def show_contacts():
    
    phone_book = []

    file = open(path_phone_book, 'r', encoding='UTF-8')
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
    print(*phone_book, sep='\n')

def add_cont():
    file = open(path_phone_book, 'a', encoding='UTF-8')
    data1 = input('введите ФИО: ')
    data2 = input('номер телефона: ')
    data3 = input('Комментарий: ')
    data = '\n' + data1 + '; ' + data2 + '; ' + data3  
    print(data)
    file.write(data)
    file.close()

def read_cont():
    file = open(path_phone_book, 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for contact in data:
        print(contact)

def find_cont():
    file = open(path_phone_book, 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    search_cont = input('введите для поиска информацию: ')
    for cont in data:
        if search_cont.lower() in cont.lower():
            print(cont)

def change_cont():
    phone_book = []

    file = open(path_phone_book, 'r', encoding='UTF-8')
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
    print(*phone_book, sep='\n')
    elem = int(input('введите id, : '))
    if elem < len(phone_book):
        print(phone_book[elem])
        corr = input('ключ, которые хотите поменять: ')
        newStr = input('на что хотите поменять: ')
        phone_book[elem][corr] = newStr
    else: print("ошибка. Приходите попозже")
    print(*phone_book, sep='\n')
    new_phone_book = ''
    i=0
    for contact in phone_book:
        new_phone_book = new_phone_book + f"{contact['name']};{contact['phone']}; {contact['comment']} \n"
    
    file = open(path_phone_book, 'w', encoding='UTF-8')
    file.write(new_phone_book)
    file.close()
    
def save_file():
    print('''тут будет функция, которая будет сохранять все изменения, но я пока не понимаю зачем она нужна.
           Чисто теоритически, можно переписать всю программу, чтобы словарь выгружался в начале и в файл записывался только при нажатии этой кнопки
            но меня смущает то, что все будет висеть в оперативной памяти, в идеале контакты должны быть базой данных, и при выборе
            этой опции будут вноситься данные в базу данных из текстового файла изменений, которые формируются сейчас...''')

def delete_cont():
    phone_book = []

    file = open(path_phone_book, 'r', encoding='UTF-8')
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
    print(*phone_book, sep='\n')
    elem = int(input('введите id, контакта, который хотите удалить : '))
    if elem < len(phone_book):
        print(phone_book[elem])
        del phone_book[elem]
    else: print("ошибка. Приходите попозже")
    print(*phone_book, sep='\n')
    new_phone_book = ''
    i=0
    for contact in phone_book:
        new_phone_book = new_phone_book + f"{contact['name']};{contact['phone']}; {contact['comment']} \n"
    print(new_phone_book)
    file = open(path_phone_book, 'w', encoding='UTF-8')
    file.write(new_phone_book)
    file.close()

show_menu = 0
path_phone_book = 'sample.txt'
while show_menu != 8:
    if show_menu == 0:
        print('''# 1. Открыть файл
# 2. Сохранить файл
# 3. Посмотреть все контакты
# 4. Создать контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход''')
        show_menu = int(input('введите цифру: '))
    if 0 < show_menu < 9:
        if show_menu == 1: path_phone_book = open_file()
        if show_menu == 2: save_file()
        if show_menu == 3: show_contacts()
        if show_menu == 4: add_cont()
        if show_menu == 5: find_cont()
        if show_menu == 6: change_cont()
        if show_menu == 7: delete_cont()
        if show_menu == 8: break
    print('^^^^^^^^^^^^^^^^^^^^^^^^')
    show_menu = 0
    
