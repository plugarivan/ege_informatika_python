"""
В текстовом файле содержится последовательность из символов X, Y, Z.
Найти максимальную длину цепочки символов, которая не содержит “XY”.
"""
with open('../files/24/zadanie24_2.txt') as f:
    s = f.readline()
    k = 1
    kmax = 0
    for i in range(1, len(s)):
        if s[i] != 'Y' and s[i-1] != 'X':
            k += 1
            if k > kmax:
                kmax = k
        else:
            k = 1
    print(kmax)