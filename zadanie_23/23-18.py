def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    return f(x - 8, y) + f(x // 2, y)

print(f(102, 43) * f(43, 5))