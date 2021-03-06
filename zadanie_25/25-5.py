'''
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [174457; 174505], числа, имеющие
ровно два различных натуральных делителя, не считая единицы и самого числа. Для каждого найденного числа запишите эти
два делителя в таблицу на экране с новой строки в порядке возрастания произведения этих двух делителей. Делители в
строке таблицы также должны следовать в порядке возрастания.
'''
for i in range(174457, 174506):
    divs = set()
    for d in range(2, round(i ** 0.5)+1):
        if i % d == 0:
            divs.add(d)
            divs.add(i // d)
            if len(divs) > 2:
                break
    if len(divs) == 2:
        print(sorted(list(divs)))