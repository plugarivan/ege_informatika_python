'''
У исполнителя Калькулятор три команды, которым присвоены номера:
1. прибавь 1
2. умножь на 2
3. умножь на 3
Сколько есть программ, которые число 1 преобразуют в число 14?
'''
def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)

print(f(1, 14))