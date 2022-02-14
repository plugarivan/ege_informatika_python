'''
Пусть M(N) - пятый по величине делитель натурального числа N без учёта самого числа и единицы.
Если у числа N меньше 5 различных делителей, не считая единицы и самого числа, считаем, что M(N) = 0.
Найдите 5 наименьших натуральных чисел, превышающих 300 000 000, для которых M(N) > 0.
В ответе запишите найденные значение M(N) в порядке возрастания соответствующих им чисел N.
'''
i = 300000001
k = 0
while k != 5:
    divs = []
    for d in range(2, round(i ** 0.5)):
        if i % d == 0:
            divs.append(d)
            if d != i // d:
                divs.append(i // d)
    divs.sort()
    if len(divs) >= 5:
        k += 1
        print(divs[-5])
    i += 1