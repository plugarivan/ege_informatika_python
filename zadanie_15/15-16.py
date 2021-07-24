"""
Обозначим через ДЕЛ (n, m) утверждение «натуральное число n делится без остатка на натуральное число m». Для какого наименьшего натурального числа А формула
ДЕЛ (x, A) → (ДЕЛ (x, 14) ∧ ДЕЛ (x, 21))
тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?
"""


def f(x, a):
    return (x % a == 0) <= ((x % 14 == 0) and (x % 21 == 0))


for a in range(1, 100):
    fl = True
    for x in range(1, 100):
        if not f(x, a):
            fl = False
            break
    if fl:
        print(a)
        break

