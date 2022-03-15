#20
def f(x, y, p):
    if x + y <= 20 or p > 3:
        return p == 3
    if p % 2:
        return f(x - 1, y, p + 1) and f(x // 2, y, p + 1) and f(x, y - 1, p + 1) and f(x, y // 2, p + 1)
    else:
        return f(x - 1, y, p + 1) or f(x // 2, y, p + 1) or f(x, y - 1, p + 1) or f(x, y // 2, p + 1)

print([i for i in range(100, 1, -1) if f(10, i, 0)])

#21
def f(x, y, p):
    if x + y <= 20 and (p == 4 or p == 2):
        return True
    else:
        if x + y > 20 and p == 4:
            return False
        else:
            if x + y <= 20:
                return False
    if p % 2 == 0:
        return f(x - 1, y, p + 1) and f(x // 2, y, p + 1) and f(x, y - 1, p + 1) and f(x, y // 2, p + 1)
    else:
        return f(x - 1, y, p + 1) or f(x // 2, y, p + 1) or f(x, y - 1, p + 1) or f(x, y // 2, p + 1)

print([i for i in range(100, 1, -1) if f(10, i, 0)])

#2324324445
#25