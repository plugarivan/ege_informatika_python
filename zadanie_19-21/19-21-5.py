#20 задача
def f(x, p):
    if x >= 48:
        return p == 3
    if p % 2:
        return f(x + 1, p + 1) and f(x + 4, p + 1) and f(x * 2, p + 1)
    else:
        return f(x + 1, p + 1) or f(x + 4, p + 1) or f(x * 2, p + 1)

print([i for i in range(1, 40) if f(i, 0)])
#21 задача
def f(x, p):
    if x >= 48 and (p == 4 or p == 2):
        return True
    else:
        if x < 48 and p == 4:
            return False
        else:
            if x >= 48:
                return False
    if p % 2:
        return f(x + 2, p + 1) or f(x + 3, p + 1) or f(x * 2, p + 1)
    else:
        return f(x + 2, p + 1) and f(x + 3, p + 1) and f(x * 2, p + 1)

print([i for i in range(1, 30) if f(i, 0)])