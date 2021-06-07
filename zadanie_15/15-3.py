"""
Для какого наименьшего целого числа А выражение
((x – 30 < A) ∧ (15 – y < A)) ∨ (x•(y+3) > 60)
тождественно истинно, т.е. принимает значение 1 при любых целых положительных x и y?
"""
def f(x, y, a):
    return ((x - 30 < a) and (15 - y < a)) or (x*(y + 3) > 60)

for a in range(1, 1000):
    answer = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(f(x, y, a)):
                answer = False
                break
    if answer:
        print(a)
        break
