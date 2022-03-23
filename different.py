def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + f(int('1' + bin(x)[2:], 2), y)

print(f(int('100', 2), int('110001', 2)))