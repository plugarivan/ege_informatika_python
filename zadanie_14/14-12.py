'''
(Б.С. Михлин) Число 538 записали в системах счисления с основаниями от 2 до 10 включительно. При каких основаниях сумма цифр этого числа четная?
В ответе укажите сумму всех подходящих оснований.
'''
summa = 0
for i in range(2, 11):
    ss = 0
    x = 538
    while x > 0:
        ss += x % i
        x //= i
    if ss % 2 == 0:
        summa += i
print(summa)