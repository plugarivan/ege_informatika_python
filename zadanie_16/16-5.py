'''
Алгоритм вычисления значения функции F(n), где n – целое число, задан следующими соотношениями:
F(n) = n, при n ≤ 5,
F(n) = n + F(n/5 + 1), когда n > 5 и делится на 5,
F(n) = n + F(n + 6) , когда n > 5 и не делится на 5.
Назовите минимальное значение n, для которого F(n) определено и больше 1000.
'''
def f(n):
    if n <= 5:
        return n
    else:
        if n % 5 == 0:
            return n + f(n/5 + 1)
        else:
            return n + f(n + 6)

for n in range(1, 1000):
    try:
        if f(n) > 1000:
            print(n)
            break
    except BaseException:
        pass

