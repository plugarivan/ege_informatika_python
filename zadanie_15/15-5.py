'''Для какого наибольшего целого неотрицательного чила А выражение
тождественно истинно, т.е. принимает значение 1 при любых целых положительных x и y.'''
def f(x, y, a):
    return (x >= a) or (y >= a) or (x * y <= 270)

for a in range(0, 1000):
    fl = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(f(x, y, a)):
                fl = False
                break
        if not(fl):
            break
    if fl:
        print(a)