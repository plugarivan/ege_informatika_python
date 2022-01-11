'''Чему равно значение функции f(25)?'''

def f(n):
    if n == 1:
        return 1
    elif n > 1:
        if n % 2 == 0:
            return 3 * f(n - 1) - 1
        else:
            return 2 * f(n - 2)

print(f(25))