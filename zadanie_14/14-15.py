'''
Укажите наименьшее основание системы счисления, в которой запись числа 86 оканчивается на 22.
'''
for n in range(3, 36):
    x = 86
    if 86 % n == 22 or (86 % n == 2 and 86 // n % n == 2):
        print(n)