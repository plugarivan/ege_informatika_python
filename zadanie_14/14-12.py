'''
Число 804 записали в системах счисления с основаниями от 2 до 10 включительно.
При каких основаниях в записи этого числа есть цифра 1? В ответе укажите сумму всех подходящих оснований.
'''
summa = 0
for n in range(2, 11):
    x = 804
    number = ''
    while x > 0:
        number = str(x % n) + number
        x //= n
    print(number)
    if number.count('1'):
        summa += n
print(summa)
