def check(value, num)
    if value == True:
        print('угадали число')
    if value == '>':
        check((num+num)//2)
    if value == '<':
         check((num)//2)
