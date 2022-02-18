lst = [1, 2, 'hello', 10, 'qwerty', 11]

print(f'На даний момент в користувача такий список: {lst}\n')           #Меню користувача
print('Дії які ви можете виконати зі списком:')
print('1)append (додати новий елемент в кінець списка);')
print('2)insert (додати новий елемент за заданий вами позицією);')
print('3)remove (видалити вибраний вами елемент);')
print('4)index (знайти позицію відповідного елемента).\n')
number = int(input('Виберіть дію (ввести потрібно тільки цифру): '))

if number == 1:                                                             #append
    type = input('Який тип елемента ви хочете додати (стрічка / цифра): ')
    elem = input('Введіть елемент: ')
    if type == 'цифра':
        elem = int(elem)
    if type == 'цифра' or type == 'стрічка':
        if elem in lst:
            check = input('Елемент вже існує, чи бажаєте додати ще один(так/ні):')
            if check == 'так':
                lst.append(elem)
                print(f'\nНовий список: {lst}')
        else:
            lst.append(elem)
    else:
        print('Ви ввели неправильний тип елемента')

if number == 2:                                                             #insert
    type = input('Який тип елемента ви хочете додати (стрічка / цифра): ')
    ind = int(input('Введіть на яку позицію ви хочете вставити елемент: '))
    elem = input('Введіть елемент: ')

    if type == 'цифра':
        elem = int(elem)
    if type == 'цифра' or type == 'стрічка':
        if elem in lst:
            check = input('Елемент вже існує, чи бажаєте додати ще один(так/ні):')
            if check == 'так':
                lst.insert(ind, elem)
                print(f'\nНовий список: {lst}')
        else:
            lst.insert(ind, elem)
    else:
        print('Ви ввели неправильний тип елемента')

if number == 3:                                                             #remove
    type = input('Який тип елемента ви хочете видалити (стрічка / цифра): ')
    elem = input('Введіть елемент: ')

    if type == 'цифра':
        elem = int(elem)
    if type != 'стрічка' and type != 'цифра':
        print('Ви ввели неправильний тип елемента')
    elif elem in lst:
        lst.remove(elem)
        print(f'Новий список: {lst}')
    else: print('Заданого елемента не найдено в списку')

if number == 4:                                                             #index
    type = input('Який тип елемента (стрічка / цифра): ')
    elem = input('Введіть елемент: ')

    if type == 'цифра':
        elem = int(elem)
    if type != 'стрічка' and type != 'цифра':
        print('Ви ввели неправильний тип елемента')
    elif elem in lst:
        print(f'Індекс елемента: {lst.index(elem)}')
    else:
        print('Заданого елемента не найдено в списку')

print('\nЗавершення роботи!')
