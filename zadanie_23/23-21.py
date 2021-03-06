'''
Исполнитель Нолик преобразует число, записанное на экране в троичной системе счисления. У исполнителя есть две команды,
которым присвоены номера:
1. Вычесть 2
2. Обнулить младший разряд
Первая команда уменьшает число на 2. Вторая команда обнуляет ненулевой младший разряд троичной записи числа.
(Например, при выполнении этой команды число 21 преобразуется в число 20.
Если в младшем разряде находится 0, то данная команда не выполняется).
Сколько существует программ, которые троичное число 212, преобразуют в троичное число 10?
'''
def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x % 3 == 0:
        return f(x - 2, y)
    return f(x - 2, y) + f(x // 3 * 3, y)

print(f(23, 3))