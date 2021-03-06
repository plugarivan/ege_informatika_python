'''
(Крылов) Исполнитель Вычислитель преобразует число, записанное на экране.
У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 2
2. Умножить на 2
3. Умножить на 3
Сколько существует программ, которые преобразут исходное число 2 в число 28 и при этом траектория вычислений, содержит число 6?
'''

def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    return f(x + 2, y) + f(x * 2, y) + f(x * 3, y)

print(f(2, 6) * f(6, 28))