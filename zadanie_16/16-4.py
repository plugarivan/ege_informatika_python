"""
f(0) = 0
f(n) = f(n/2), если n > 0 и при этом n четно
f(n) = 1 + f(n - 1), если n нечетно
Назовите минимальное значение n, для которого f(n) = 11
"""
def f(n):
    if n == 0:
        return 0
    else:
        if n % 2 == 0:
            return f(n // 2)
        else:
            return 1 + f(n - 1)

for n in range(1, 10000):
    if f(n) == 11:
        print(n)
        break
