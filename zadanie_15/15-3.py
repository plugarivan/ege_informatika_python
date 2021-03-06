'''
На числовой прямой даны отрезки A = [30; 62], B = [25; 38] и C = [40; N] и функция
F(x) = ( (x  B)   (x  A) )  ( (x  C)  (x  B) )
При каком наименьшем числе N функция F(x) истинна более чем для 20 целых чисел x?
'''


def f(x, n):
    return ((not(25 <= x <= 38)) <= (not(30 <= x <= 62))) and ((not(40 <= x <= n)) <= (25 <= x <= 38))


for n in range(1, 100):
    s = set()
    for x in range(1, 1000):
        if f(x, n):
            s.add(x)
    if len(s) > 20:
        print(n)
        break