"""
На числовой прямой задан отрезок A. Известно, что формула
((x ∈ A) → (x2 ≤ 100)) ∧ ((x2 ≤ 64) → (x ∈ A))
тождественно истинна при любом вещественном x. Какую наибольшую длину может иметь отрезок A?
"""
def f(x, a1, a2):
    return ((a1 <= x <= a2) <= (x*x <= 100)) and ((x*x <= 64) <= (a1 <= x <= a2))

s = []
for a1 in range(-100, 100):
    for a2 in range(-100, 100):
        fl = True
        for x in range(-100, 100):
            if not(f(x, a1, a2)):
                fl = False
                break
        if fl:
            s.append(a2 - a1)
print(max(s))