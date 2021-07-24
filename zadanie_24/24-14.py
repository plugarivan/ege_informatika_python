"""
Текстовый файл 24-j5.txt состоит не более чем из 106 символов S, T, O, C, K.
Сколько раз встречается в файле комбинация «OKTOS»?
"""
with open('../files/24/24-j5.txt') as f:
    s = f.readline()
    print(s.count('OKTOS'))
