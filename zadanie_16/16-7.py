'''
Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = n при n > 18
F(n) = 3·F(n+1) + n + 8, если n ≤ 18
Чему равно значение функции F(9)?
'''
def f(n):
    if n > 18:
        return n
    else:
        return 3 * f(n + 1) + n + 8

print(f(9))