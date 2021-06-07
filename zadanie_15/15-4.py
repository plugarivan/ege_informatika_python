"""
Укажите наибольшее целое значение А, при котором выражение
(y + 5x ≠ 80) ∨ (3x > A) ∨ (y > A)
истинно для любых целых положительных значений x и y.
"""
def f(x, y, a):
    return ((y + 5*x) != 80) or (3 * x > a) or (y > a)

for a in range(1, 100):
    answer = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not(f(x, y, a)):
                answer = False
                break
    if answer:
        print(a)
