"""
У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 1
2. Прибавить 2
3. Умножить на 3
Сколько существует программ, которые преобразуют исходное число 2 в число 16, при этом
траектория вычислений содержит число 11 и не содержить числа 15?
"""
def f(x, y):
    if x > y or y == 15:
        return 0
    if x == y:
        return 1
    if y % 3 == 0:
        return f(x, y - 1) + f(x, y - 2) + f(x, y // 3)
    return f(x, y - 1) + f(x, y - 2)

print(f(2, 11) * f(11, 16))