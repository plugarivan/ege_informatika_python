"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [154026; 154043], числа,
имеющие ровно 4 различных делителя.
В ответе для каждого найденного числа запишите два его наибольших делителя в порядке возрастания.
"""
import time
start_time = time.time()

for i in range(154026, 154044):
    divs = set()
    for d in range(1, round(i**0.5) + 1):
        if i % d == 0:
            divs.add(d)
            divs.add(i // d)
            if len(divs) > 4:
                break
    if len(divs) == 4:
        print(divs)

print("{:.3f}s".format(time.time() - start_time))