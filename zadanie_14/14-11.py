''' Число 559 записали в системах счисления с основаниями от 2 до 10 включительно.
При каких основаниях сумма цифр этого числа нечетная? В ответе укажите сумму всех подходящих оснований.'''
k = 0
for i in range(2, 11):
    x = 559
    s = 0
    while x > 0:
        s += x % i
        x //= i
    if s % 2 != 0:
        k += i
print(k)