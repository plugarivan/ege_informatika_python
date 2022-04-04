'''
Автомат обрабатывает натуральное число N<256 по следующему алгоритму:
1) Строится восьмибитная двоичная запись числа N-1.
2) Инвертируются все разряды исходного числа (0 заменяется на 1, 1 на 0).
3) Полученное число переводится в десятичную систему счисления.
Чему равен результат работы алгоритма для N = 178?
'''
s = bin(178 - 1)[2:]
s = (8 - len(s)) * '0' + s
s1 = ''
for x in s:
    if x == '1':
        s1 += '0'
    else:
        s1 += '1'
print(int(s1, 2))