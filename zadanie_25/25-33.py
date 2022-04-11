'''
Среди целых чисел, принадлежащих числовому отрезку [298435; 363249], найдите числа, которые представляют собой
произведение двух различных простых делителей. Запишите в ответе количество таких чисел и то из них, которое ближе всего к их среднему арифметическому.
'''
def prost(n):
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

minimum = 1000000000000
done = []
for i in range(298435, 363250):
    for d in range(2, round(i ** 0.5)):
        if d * (i // d) == i and prost(d) and prost(i // d):
            done.append(i)
sred = sum(done) //  len(done)
for i in range(298435, 363250):
    if i in done and abs(sred - i) < minimum:
        minimum = abs(sred - i)
        g = i
print(len(done), g)
