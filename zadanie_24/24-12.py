'''
Текстовый файл 24-j5.txt состоит не более чем из 10**6 символов S, T, O, C, K. Сколько раз встречается в файле комбинация «KOT»?
'''
with open('../files/24/24-j5.txt') as f:
    s = f.readline()
    print(s.count('KOT'))