def f(x, y, p):
    if x + y >= 67 or p > 4:
        return p == 4
    if p % 2:
        return f(x + 1, y, p + 1) or f(x + y, y, p + 1) or f(x, y + 1, p + 1) or f(x, y + x, p + 1)
    else:
        return f(x + 1, y, p + 1) and f(x + y, y, p + 1) and f(x, y + 1, p + 1) and f(x, y + x, p + 1)

for i in range(1, 100):
    if f(9, i, 1):
        print(i)