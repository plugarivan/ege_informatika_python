"""
Чему равно значение функции F(26)?
"""

def f(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return n + f(n - 1)
        else:
            return 2 * f(n - 2)

print(f(26))
