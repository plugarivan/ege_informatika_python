'''
На числовой прямой даны два отрезка: P = [15, 20] и Q = [5, 38]. Найдите наибольшую возможную длину отрезка A, при котором формула
( (x ∈ А) → (x ∈ P) ) ∨ (x ∈ Q)
тождественно истинна, то есть принимает значение 1 при любых x.
'''
p = set(range(15, 21))
q = set(range(5, 39))
a = set(range(-1000, 1000))
for x in range(-1000, 1000):
    if not(((x in a) and (x in p)) or (x in q)):
        a.remove(x)
print(max(a) - min(a))