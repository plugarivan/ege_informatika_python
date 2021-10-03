"""Найдите все натуральные числа, принадлежащие отрезку [106000000, 107000000],
у которых ровно три различных чётных делителя. В ответе перечислите найденные числа в порядке возрастания"""
import time
start_time = time.time()

for i in range(106000000, 107000001, 2):
    divs = 1 #так как число четное, минимум один делитель у него уже есть
    for d in range(2, round(i ** 0.5) + 1):
        if i % d == 0:
            if d % 2 == 0:
                divs += 1
            if (i // d) % 2 == 0:
                divs += 1
        if i ** 0.5 == round(i ** 0.5):
            divs -= 1
        if divs > 3:
            break
    if divs == 3:
        print(i)


print("{:.3f}s".format(time.time() - start_time))