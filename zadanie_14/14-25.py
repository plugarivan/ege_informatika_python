'''
В какой системе счисления выполняется равенство 12X · 31X = 402X? В ответе укажите число – основание системы счисления.
'''
for x in range(5, 30):
    if int('12', x) * int('31', x) == int('402', x):
        print(x)