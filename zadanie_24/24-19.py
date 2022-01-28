'''
(П.Е. Финкель) Текстовый файл 24-1.txt состоит не более чем из 10**6 символов - заглавных латинских букв и цифр.
Определите максимальное число, состоящее только из чётных цифр. Под числом подразумевается последовательность цифр,
ограниченная другими символами (не цифрами).
'''
with open('../files/24/24-1.txt') as f:
    s = f.readline()
    s1 = ''
    numbers = []
    maximum = 0
    for c in s:
        if c.isdigit():
            s1 += c
        else:
            if s1 != '':
                numbers.append(s1)
            s1 = ''
    for i in numbers:
        k = 0
        x = int(i)
        while x > 0:
            if x % 2 == 0:
                k += 1
            x //= 10
        if k == len(i):
            maximum = max(maximum, int(i))
print(maximum)


