"""
(№ 2229) (М.В. Кузнецова) Значение арифметического выражения: 9**8 + 3**25 – 14 записали в системе счисления с основанием 3.
Найдите сумму цифр в этой записи. Ответ запишите в десятичной системе.
"""
x = 9**8 + 3**25 - 14
s = 0
while x > 0:
    s += x % 3
    x = x // 3
print(s)