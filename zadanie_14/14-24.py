'''
(П.М. Волгин) Значение арифметического выражения 26**2 + 169 - 11 записали в системе счисления с основанием 13.
В этой записи помимо цифр от 0 до 9 могут встречаться цифры из списка: А, B, С, которые имеют числовые значения от 10 до 12 соответственно.
Сколько цифр C и цифр 2 встречается в этой записи?
'''
x = 26 ** 2 + 169 - 11
k = 0
while x > 0:
    if x % 13 == 12 or x % 13 == 2:
        k += 1
    x //= 13
print(k)