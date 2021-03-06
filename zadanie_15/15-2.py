'''
На числовой прямой даны два отрезка: P=[20,50] и Q=[10,60]. Определите наибольшую возможную длину отрезка A,
при котором формула
((x ∈ P) → (x ∈ А)) ∧ ((x ∈ A) → (x ∈ Q))
тождественно истинна, то есть принимает значение 1 при любом значении переменной х.
'''
def f(a1, a2, x):
    return ((20 <= x <= 50) <= (a1 <= x <= a2)) and ((a1 <= x <= a2) <= (10 <= x <= 60))

s = []
for a1 in range(-100, 100):
    for a2 in range(-100, 100):
        flag = True
        for x in range(-100, 100):
            if not(f(a1, a2, x)):
                flag = False
                break
        if flag:
            s.append(a2-a1)
print(max(s))