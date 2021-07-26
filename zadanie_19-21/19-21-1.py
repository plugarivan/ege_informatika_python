def f(x, y, p):
    if x + y >= 75 and (p == 5 or p == 3):
        return 1
    else:
        if x + y < 75 and p == 5:
            return 0
        else:
            if x + y >= 75:
                return 0
    if p % 2:
        return f(x + 3, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 3, p + 1) and f(x, y * 2, p + 1)
    else:
        return f(x + 3, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 3, p + 1) or f(x, y * 2, p + 1)

for i in range(1, 100):
    if f(9, i, 1):
        print(i)