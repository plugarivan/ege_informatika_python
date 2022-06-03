'''
Автомат обрабатывает натуральное число N < 256 по следующему алгоритму:
1) Строится восьмибитная двоичная запись числа N.
2) Инвертируются все разряды исходного числа, кроме последней единицы и стоящих за ней нулей (0 заменяется на 1, 1 на 0).
3) Полученное число переводится в десятичную систему счисления.
Для какого значения N результат работы алгоритма равен 221?
'''
for n in range(1, 256):
    s = bin(n)[2:]
    s = (8 - len(s)) * '0' + s
    s1 = ''
    i = 0
    for x in range(len(s)):
        if s[x] == '1':
            i += 1
            if i == s.count('1'):
                i = x
    for x in range(0, i):
        if s[x] == '1':
            s1 += '0'
        if s[x] == '0':
            s1 += '1'
    for x in range(i, len(s)):
        s1 += s[x]
    if int(s1, 2) == 221:
        print(n)