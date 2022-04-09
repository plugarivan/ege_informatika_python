'''
Текстовый файл 24-196.txt содержит строку из заглавных латинских букв X, Y и Z, всего не более чем из 106 символов.
Определите максимальное количество идущих подряд пар символов ZX или ZY.
'''
with open('../files/24/24-196.txt') as f:
    s = f.readline()
    s = s.replace('Y', 'X')
    s = s.replace('ZX', '.')
    k, kmax = 0, 0
    for c in s:
        if c == '.':
            k += 1
            kmax = max(k, kmax)
        else:
            k = 0
    print(kmax)