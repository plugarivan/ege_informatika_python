'''
(М.В. Кузнецова) Значение арифметического выражения: 9 ** 5 + 3**25 – 20 записали в системе счисления с основанием 3.
Найдите сумму цифр в этой записи. Ответ запишите в десятичной системе.
'''
x = 9 ** 5 + 3 ** 25 - 20
summa = 0
while x > 0:
    summa += x % 3
    x //= 3
print(summa)