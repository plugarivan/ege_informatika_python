'''
(Крылов) Определите максимальное количество идущих подряд символов, расположенных в алфавитном порядке (возможно, с повторением символов).
'''
with open('../files/24/24 варианты 5-9.txt') as f:
    s = f.readline()
    k, kmax = 1, 1
    for i in range(1, len(s)):
        if s[i] >= s[i-1]:
            k += 1
            kmax = max(k, kmax)
        else:
            k = 1
print(kmax)
