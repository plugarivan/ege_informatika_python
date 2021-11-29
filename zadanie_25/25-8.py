'''
(Б.С. Михлин) Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [586132; 586430],
числа, имеющие максимальное количество различных делителей. Найдите минимальное и максимальное из таких чисел.
Для каждого из них в отдельной строчке выведите количество делителей и наибольший делитель, не равный самому числу.
'''
maximum_divs = 0
for i in range(586132, 586431):
    divs = set()
    for d in range(1, round(i ** 0.5) + 1):
        if i % d == 0:
            divs.add(d)
            divs.add(i // d)
    maximum_divs = max(len(divs), maximum_divs)
print(maximum_divs)

for i in range(586132, 586431):
    divs = set()
    for d in range(1, round(i ** 0.5) + 1):
        if i % d == 0:
            divs.add(d)
            divs.add(i // d)
    if len(divs) == maximum_divs:
        print(sorted(list(divs))[-2],sorted(list(divs))[-3], i)
