'''
(Пробный КЕГЭ, 2022) Определите количество семизначных чисел, записанных в семеричной системе счисления, учитывая,
что числа не могут начинаться с цифр 3 и 5 и не должны содержать сочетания цифр 22 и 44 одновременно.
'''
from itertools import product
numbers = product('0123456', repeat=7)
k = 0
for n in numbers:
    number = ''.join(n)
    if number[0] not in '035' and (('44' in number and '22' not in number) or ('44' not in number and '22' in number) or ('44' not in number and '22' not in number)):
        k += 1
print(k)