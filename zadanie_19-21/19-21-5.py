#20 задача
def f(x, p):
    if x >= 29:
        return p == 4
    if p % 2:
        return f(x + 1, p + 1) or f(x + 2, p + 1) or f(x * 2, p + 1)
    else:
        return f(x + 1, p + 1) and f(x + 2, p + 1) and f(x * 2, p + 1)

print([i for i in range(1, 100) if f(i, 0)])
#21 задача
def f(x, y, p):
    if x + y >= 77 and (p == 5 or p == 3):
        return True
    else:
        if x + y < 77 and p == 5:
            return False
        else:
            if x + y >= 77:
                return False
    if p % 2:
        return f(x + 1, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 2, p + 1)
    else:
        return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 2, p + 1)

print(min([i for i in range(1, 100) if f(7, i, 1)]))