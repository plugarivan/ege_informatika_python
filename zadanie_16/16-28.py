'''
Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число, задан следующими соотношениями:
F(0) = 8
F(n) = 5 + F(n / 3) если n > 0 и n делится на 3
F(n) = F(n // 3) в остальных случаях
Здесь // означает деление нацело. Определите количество значений n на отрезке [1, 100 000 000], для которых F(n) = 18.
'''
s = 100000000 * [0]
for n in range(len(s)):
    if n == 0:
        s[n] = 8
    else:
        if n % 3 == 0:
            s[n] = 5 + s[n // 3]
        else:
            s[n] = s[n // 3]

print(s.count(18))