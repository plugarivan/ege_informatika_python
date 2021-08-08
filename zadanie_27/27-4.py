"""
Набор данных состоит из нечетного количества пар натуральынх чисел. Необходимо выбрать из каждой пары ровно одно
число так, что бы чётность суммы выбранных чисемл совпадала с чётностью большинства выбранных чисел и при этом сумма
выбранных чисел была как можно меньше. Определите минимальную сумму которую можно получить при таком выборе.
"""
with open('../files/27/s27-B.txt') as f:
    n = f.readline()
    summa, chet, nechet, dnech1, dnech2, dch1, dch2 = 0, 0, 0, 10001, 10001, 10001, 10001
    for x in f:
        a, b = map(int, x.split())
        mn = min(a, b)
        mx = max(a, b)
        summa += mn
        if mn % 2 == 0:
            chet += 1
        else:
            nechet += 1
        if a % 2 != b % 2:
            if mn % 2 == 0:
                if mx - mn < dch1:
                    dch2 = dch1
                    dch1 = mx - mn
                if mx - mn < dch2:
                    dch2 = mx - mn
            if mn % 2 != 0:
                if mx - mn < dnech1:
                    dnech2 = dnech1
                    dnech1 = mx - mn
                if mx - mn < dnech2:
                    dnech2 = mx - mn

    print(summa)
    print(chet, nechet)
    print(dch1, dch2, dnech1, dnech2)