"""
Для какого наибольшего целого неотрицательного числа A выражение
(2x + 3y < 30) ∨ (x + y ≥ A)
тождественно истинно при любых целых неотрицательных x и y?
"""
def f(x, y, a):
    return (2*x + 3*y < 30) or (x + y >= a)

for a in range(0, 100):
    fl = True
    for x in range(0, 100):
        for y in range(0, 100):
            if not(f(x, y, a)):
                fl = False
                break
    if fl:
        print(a)