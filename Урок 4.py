dct = {'person': {'in_dict': [1, 2, 3],

                  'after_list': {4, '5'},

                  'after_set': ('hello', )}}

key1 = []
value1 = []

for i in dct.values():
    for key, value in i.items():
        key1.append(key)
        value1.append(value)

for i in value1:
    for j in i:
        key1.append(j)
        value1.append('')

new_dct = {key: value for key, value in zip(key1, value1)}

print(new_dct)
