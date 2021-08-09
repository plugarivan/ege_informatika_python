"""
В текстовом файле записан набор натуральных чисел, не превышающих 10**8. Гарантируется, что все числа различны.
Из набора нужно выбрать три числа, сумма которых делится на 3. Какую наибольшую сумму можно при этом получить?
"""
with open('../files/27/ss27-B.txt') as f:
    n = int(f.readline())
    ost0, ost1, ost2 = [], [], []
    for x in f:
        a = int(x)
        if a % 3 == 0:
            ost0.append(a)
        elif a % 3 == 1:
            ost1.append(a)
        else:
            ost2.append(a)
    ost0.sort(reverse=True)
    ost1.sort(reverse=True)
    ost2.sort(reverse=True)
    print(sum(ost0[:3]))
    print(sum(ost1[:3]))
    print(sum(ost2[:3]))
    print(ost0[1] + ost1[1] + ost2[2])
