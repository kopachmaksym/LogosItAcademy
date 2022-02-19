lst = [1, 2, 5, 'hello', 'kol', 4, 10, 1]
var = 'так'
print('\t\t1.Вивести елементи на екран (звичайний юзер)\n\t\t2.Редагувти список, як адмін')
menu = int(input('\n\t\tВидеріть дію (потрібно ввести цифру): '))

if menu == 1:
    print(f'\n\t\tЕлементи списка: {lst}')

elif menu == 2:
    print('\n\t\tДля редагування списка потрібно ввійти як адмін')
    login, password = input('\t\tВведіть логін та пароль: ').split()
    if login == 'admin' and password == '12345':
        print(f'\n\t\tВітаю, {login}!')

        while var == 'так':
            print(f'\t\tЕлементи списка: {lst}')
            print(f'\n\t\tМетоди використання у списках:')
            print('\t\t\t1)append\n\t\t\t2)insert\n\t\t\t3)remove\n\t\t\t4)index\n\t\t\t5)reverse\n\t\t\t6)clear\n\t\t\t7)count\n\t\t\t8)pop\n\t\t\t9)sort')
            number = int(input('\tВиберіть дію (потрібно ввести цифру): '))

            if number == 1:
                type = input('\tЯкий тип елемента ви хочете додати (стрічка / цифра): ')
                elem = input('\tВведіть елемент: ')
                if type == 'цифра':
                    elem = int(elem)
                if type == 'цифра' or type == 'стрічка':
                    if elem in lst:
                        check = input('\tЕлемент вже існує, чи бажаєте додати ще один(так/ні):')
                        if check == 'так':
                            lst.append(elem)
                            print(f'\n\tНовий список: {lst}')
                    else:
                        lst.append(elem)
                        print(f'\n\tНовий список: {lst}')
                else:
                    print('\tВи ввели неправильний тип елемента')

            elif number == 2:  # insert
                type = input('\tЯкий тип елемента ви хочете додати (стрічка / цифра): ')
                ind = int(input('\tВведіть на яку позицію ви хочете вставити елемент: '))
                elem = input('\tВведіть елемент: ')

                if type == 'цифра':
                    elem = int(elem)
                if type == 'цифра' or type == 'стрічка':
                    if elem in lst:
                        check = input('\tЕлемент вже існує, чи бажаєте додати ще один(так/ні):')
                        if check == 'так':
                            lst.insert(ind, elem)
                            print(f'\n\tНовий список: {lst}')
                    else:
                        lst.insert(ind, elem)
                        print(f'\n\tНовий список: {lst}')
                else:
                    print('\tВи ввели неправильний тип елемента')

            elif number == 3:  # remove
                type = input('\tЯкий тип елемента (стрічка / цифра): ')
                elem = input('\tВведіть елемент: ')
                if type == 'стрічка' or type == 'цифра':
                    if type == 'цифра':
                        elem = int(elem)
                    if elem in lst:
                        lst.remove(elem)
                        print(f'\tНовий список: {lst}')
                    else:
                        print('\tЗаданого елемента не найдено в списку')
                else:
                    print('\tВи ввели неправильний тип елемента')

            elif number == 4:  # index
                type = input('\tЯкий тип елемента (стрічка / цифра): ')
                elem = input('\tВведіть елемент: ')
                if type == 'стрічка' or type == 'цифра':
                    if type == 'цифра':
                        elem = int(elem)
                    if elem in lst:
                        print(f'\tІндекс елемента: {lst.index(elem)}')
                    else:
                        print('\tЗаданого елемента не найдено в списку')
                else: print('\tВи ввели неправильний тип елемента')

            elif number == 5:  # reverse
                lst.reverse()
                print(f'\tНовий список: {lst}')

            elif number == 6: #clear
                lst.clear()
                print(f'\tНовий список: {lst}')

            elif number == 7:  # count
                type = input('\tЯкий тип елемента (стрічка / цифра): ')
                if type == 'цифра' or type == 'стрічка':
                    elem = input('\tВведіть елемент: ')
                    if type == 'цифра':
                        elem = int(elem)
                    print(f'\tКількість похожих елементів: {lst.count(elem)}')
                else:print('\tНеправильний тип елемента')

            elif number == 8:  # pop
                ind = int(input('\tВведіть яку позицію потрібно видалити: '))
                if len(lst)-1 >= ind:
                    lst.pop(ind)
                    print(f'\tНовий список: {lst}')
                else: print('\tВибрана вами позиція за межами списка')

            elif number == 9:  # sort
                lst_for_int = [i for i in lst if type(i) == int]
                lst_for_str = [i for i in lst if type(i) == str]
                lst_for_int.sort()
                lst.clear()
                lst.extend(lst_for_int)
                lst.extend(lst_for_str)
                lst_for_int.clear()
                lst_for_str.clear()
                print(f'\tНовий список: {lst}')

            elif number not in range(1,9):
                print ('\nНе вибрана дія (1-9)')

            var = input('\nПродовжити роботу (так/ні): ')
            while True:
                if var == 'так' or var == 'ні':
                    break
                else: var = input('\nПродовжити роботу (так/ні): ')

    else:
        print('\n\t\tНеправильно введені дані')

print ('\n\t\tЗавершення роботи.')

