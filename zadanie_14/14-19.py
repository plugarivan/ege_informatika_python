'''
Сколько единиц в двоичной записи числа 4**2014 + 2**2015 – 8
'''
x = 4 ** 2014 + 2 ** 2015 - 8
k = 0
while x > 0:
    if x % 2 == 1:
        k += 1
    x //= 2
print(k)

print(bin(4 ** 2014 + 2 ** 2015 - 8).count('1'))