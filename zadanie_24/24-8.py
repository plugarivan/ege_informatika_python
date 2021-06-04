"""
Текстовый файл состоит не более чем из 106 символов A, B и C. Определите максимальную длину цепочки вида ABABAB...
(составленной из фрагментов AB, последний фрагмент может быть неполным).
"""
with open('../files/24/zadanie24_1.txt') as f:
    s = f.readline()
    k = 0
    kmax = 0
    for c in s:
        if (c == 'A' and k % 2 == 0) or (c == 'B' and k % 2 == 1):
            k += 1
            if k > kmax:
                kmax = k
        elif c == 'A':
            k = 1
        else:
            k = 0
    print(kmax)
