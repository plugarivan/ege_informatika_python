'''
(А.М. Кабанов) В текстовом файле k7a-2.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F. Найдите длину самой длинной подцепочки, состоящей из символов A, C, D (в произвольном порядке).
'''
with open('../files/24/k7a-2.txt') as f:
    s = f.readline()
    k, kmax = 0, 0
    for i in s:
        if i == 'D' or i == 'A' or i == 'C':
            k += 1
            kmax = max(k, kmax)
        else:
            k = 0
    print(kmax)