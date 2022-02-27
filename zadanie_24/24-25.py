'''
(Крылов) Определите максимальное количество идущих подряд символовЮ среди которых нет символа Z.
'''
with open('../files/24/24 варианты 5-9.txt') as f:
    s = f.readline()
    k, kmax = 1, 1
    for i in range(1, len(s)):
        if s[i] == 'Z' or s[i-1] == 'Z':
            k = 1
        else:
            k += 1
            kmax = max(k, kmax)
print(kmax)