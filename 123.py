def lst_to_dct_1 (keys, values):
    value_2 = []
    for i in range(n):
        value_2.append(values)
    dict = {key: value for key, value in zip(keys, value_2)}
    return dict

def lst_to_dct_2 (key1, value1=[]):
    if value1 == []:
        value1=''
        for i in key1:
            value1 = list(value1)
            value1.append('')
    dict={key: value for key,value in zip(key1,value1)}
    for i in range(len(key1)):
        dict.setdefault(key1[i], value1[i])
    return dict

q = int(input('Завдання 1 чи 2: '))
if q == 2:
    lst_1 = []
    lst_2 = []
    n = int(input('Введіть кількість елементів: '))
    for i in range(n):
        print('Тип даних:\n1)Число\n2)Стрічка\n3)кортеж\n4)незмінювана множина\n5)змінювана множина')
        var = int(input(f'Виберіть тип даних для {i + 1} елемента: '))
        while var <= 1 and var >= 5:
            var = int(input(f'Виберіть тип даних для {i+1} елемента: '))
        if var == 1:
            lst_1.append(int(input('Введіть число: ')))
        elif var == 2:
            lst_1.append(input('Введіть строку: '))
        elif var == 3:
            lst_to_tupl = []
            n_1 = int(input('Введіть кількість елементів: '))
            for i in range (n_1):
                print('Тип даних:\n1)Число\n2)Стрічка')
                var_1 = int(input('Виберіть тип: '))
                if var_1 == 1:
                    lst_to_tupl.append(int(input('Введіть число:')))
                elif var_1 == 2:
                    lst_to_tupl.append(input('Введіть строку:'))
            lst_to_tupl = tuple(lst_to_tupl)
            lst_1.append(tuple(lst_to_tupl))
        elif var == 4:
            lst_to_set = []
            n_1 = int(input('Введіть кількість елементів: '))
            for i in range(n_1):
                print('Тип даних:\n1)Число\n2)Стрічка')
                var_1 = int(input('Виберіть тип: '))
                if var_1 == 1:
                    lst_to_set.append(int(input('Введіть число:')))
                elif var_1 == 2:
                    lst_to_set.append(input('Введіть строку:'))
            lst_to_set = frozenset(lst_to_set)
            lst_1.append(lst_to_set)
        elif var == 5:
            lst_to_set = []
            n_1 = int(input('Введіть кількість елементів: '))
            for i in range(n_1):
                print('Тип даних:\n1)Число\n2)Стрічка')
                var_1 = int(input('Виберіть тип: '))
                if var_1 == 1:
                    lst_to_set.append(int(input('Введіть число:')))
                elif var_1 == 2:
                    lst_to_set.append(input('Введіть строку:'))
            lst_to_set = set(lst_to_set)
            lst_1.append(lst_to_set)

    lst_3=[]
    for i in lst_1:
        one = set()
        two = frozenset()
        if type(i) != type(one) and type(i) != type(two):
            lst_3.append(i)

    n = int(input('Введіть кількість елементів: '))
    for i in range(n):
        print('Тип даних:\n1)Число\n2)Стрічка\n3)кортеж\n4)незмінювана множина\n5)змінювана множина')
        var = int(input(f'Виберіть тип даних для {i + 1} елемента: '))
        while var <= 1 and var >= 5:
            var = int(input(f'Виберіть тип даних для {i+1} елемента: '))
        if var == 1:
            lst_2.append(int(input('Введіть число: ')))
        elif var == 2:
            lst_2.append(input('Введіть строку: '))
        elif var == 3:
            lst_to_tupl = []
            n_1 = int(input('Введіть кількість елементів: '))
            for i in range(n_1):
                print('Тип даних:\n1)Число\n2)Стрічка')
                var_1 = int(input('Виберіть тип: '))
                if var_1 == 1:
                    lst_to_tupl.append(int(input('Введіть число:')))
                elif var_1 == 2:
                    lst_to_tupl.append(input('Введіть строку:'))
            lst_to_tupl = tuple(lst_to_tupl)
            lst_2.append(tuple(lst_to_tupl))
        elif var == 4:
            lst_to_set = []
            n_1 = int(input('Введіть кількість елементів: '))
            for i in range(n_1):
                print('Тип даних:\n1)Число\n2)Стрічка')
                var_1 = int(input('Виберіть тип: '))
                if var_1 == 1:
                    lst_to_set.append(int(input('Введіть число:')))
                elif var_1 == 2:
                    lst_to_set.append(input('Введіть строку:'))
            lst_to_set = frozenset(lst_to_set)
            lst_2.append(lst_to_set)
        elif var == 5:
            lst_to_set = []
            n_1 = int(input('Введіть кількість елементів: '))
            for i in range(n_1):
                print('Тип даних:\n1)Число\n2)Стрічка')
                var_1 = int(input('Виберіть тип: '))
                if var_1 == 1:
                    lst_to_set.append(int(input('Введіть число:')))
                elif var_1 == 2:
                    lst_to_set.append(input('Введіть строку:'))
            lst_to_set = set(lst_to_set)
            lst_2.append(lst_to_set)


    dct = lst_to_dct_2(lst_3, lst_2)
    print(dct)
elif q == 1:
    keys = []
    value = []
    var_1 = int(input('Один список чи два: '))
    n = int(input('Введіть кількість ключів у словику: '))

    for i in range(n):
        print('Тип даних:\n1)Число\n2)Стрічка\n3)кортеж')
        var = int(input(f'Виберіть тип даних для ключа №{i + 1}: '))
        if var == 1:
            keys.append(int(input('Введіть число: ')))
        elif var == 2:
            keys.append(input('Введіть строку: '))
        elif var == 3:
            lst_to_tupl = []
            n_1 = int(input('Введіть кількість елементів: '))
            for i in range(n_1):
                print('Тип даних:\n1)Число\n2)Стрічка')
                var_1 = int(input('Виберіть тип: '))
                if var_1 == 1:
                    lst_to_tupl.append(int(input('Введіть число:')))
                elif var_1 == 2:
                    lst_to_tupl.append(input('Введіть строку:'))
            lst_to_tupl = tuple(lst_to_tupl)
            keys.append(tuple(lst_to_tupl))

    if var_1 == 2:
        for i in range(n):
            print('Тип даних:\n1)Число\n2)Стрічка\n3)кортеж')
            var = int(input(f'Виберіть тип даних для елемента: '))
            if var == 1:
                value.append(int(input('Введіть число: ')))
            elif var == 2:
                value.append(input('Введіть строку: '))
            elif var == 3:
                lst_to_tupl = []
                n_1 = int(input('Введіть кількість елементів: '))
                for i in range(n_1):
                    print('Тип даних:\n1)Число\n2)Стрічка')
                    var_1 = int(input('Виберіть тип: '))
                    if var_1 == 1:
                        lst_to_tupl.append(int(input('Введіть число:')))
                    elif var_1 == 2:
                        lst_to_tupl.append(input('Введіть строку:'))
                lst_to_tupl = tuple(lst_to_tupl)
                value.append(tuple(lst_to_tupl))
    dct = lst_to_dct_1(keys, value)
    print(dct)
