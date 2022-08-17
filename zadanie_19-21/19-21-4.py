#19 задача
def f(x, y, p):
    if x + y >= 81 and p == 2:
        return True
    else:
        if x + y < 81 and p == 2:
            return False
    return f(x + 1, y, p + 1) or f(x + y, y, p + 1) or f(x, y + 1, p + 1) or f(x, y + x, p + 1)

print(min([i for i in range(1, 74) if f(7, i, 0)]))
#20 задача
def f(x, y, p):
    if x + y >= 93 or p > 3:
        return p == 3
    if p % 2:
        return f(x + 1, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 2, p + 1)
    else:
        return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 2, p + 1)

print([i for i in range(1, 100) if f(12, i, 0)])
#21 задача
def f(x, y, p):
    if x + y >= 81 and (p == 4 or p == 2):
        return True
    else:
        if x + y < 81 and p == 4:
            return False
        else:
            if x + y >= 81:
                return False
    if p % 2 == 0:
        return f(x + 1, y, p + 1) and f(x + y, y, p + 1) and f(x, y + 1, p + 1) and f(x, y + x, p + 1)
    else:
        return f(x + 1, y, p + 1) or f(x + y, y, p + 1) or f(x, y + 1, p + 1) or f(x, y + x, p + 1)

print(min([i for i in range(1, 74) if f(7, i, 0)]))