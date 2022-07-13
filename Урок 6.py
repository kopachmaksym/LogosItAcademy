lst = []

n = int(input('Введіть кількість елементів(для 1 і 2 завдання): '))
for i in range(n):
    var = int(input('1)Цифра\n2)Стрічка\n\tВведіть цифру: '))
    if var == 1:
        lst.append(int(input('Введіть цифру: ')))
    elif var == 2:
        lst.append(input('Введіть цифру: '))

print(list(map(lambda i: str(i) if type(i) == int else int(i) ,lst))) #1

def func(i):    #2
    if type(i) == str:
        i = int(i)
    else:
        i = str(i)
    return i
lst_new = list(map(func,lst))
print(lst_new)

def func_2(*args): #3
    def maps(i):
        if type(i) == str:
            i = int(i)
        if type(i) == list:
            return
        return i
    st = list(map(maps,args))
    st = set(st[0:9])
    print(st)

func_2(1,[1],[3,5],'2')
