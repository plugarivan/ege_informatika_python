'''В системе счисления с основанием N запись числа 41 оканчивается на 2, а запись числа 131 — на 1.
Чему равно число N?'''
for n in range(3, 100):
    if 41 % n == 2 and 131 % n == 1:
        print(n)