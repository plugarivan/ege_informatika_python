'''
Текстовый файл 24.txt состоит не более чем из 106 символов X, Y и Z. Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
'''
with open('../files/24/24.txt') as f:
    s = f.readline()
    k, kmax = 1, 0
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            k += 1
            kmax = max(k, kmax)
        else:
            k = 1
    print(kmax)