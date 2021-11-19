'''
'''
#20 задача
def f(x, y, p):
    if x + y >= 82 or p > 3:
        return p == 3 #петя выиграл вторым ходом
    if p % 2:
        return f(x + 1, y, p + 1) and f(x * 4, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 4, p + 1)
    else:
        return f(x + 1, y, p + 1) or f(x * 4, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 4, p + 1)

print([i for i in range(1, 100) if f(4, i, 0)])
#21 задача
def f(x, y, p):
    if x + y >= 82 and (p == 4 or p == 2):
        return True
    else:
        if x + y < 82 and p == 4:
            return False
        else:
            if x + y >= 82: #перебор камней
                return False
    if p % 2 == 0:
        return f(x + 1, y, p + 1) and f(x * 4, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 4, p + 1)
    else:
        return f(x + 1, y, p + 1) or f(x * 4, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 4, p + 1)

print(min([i for i in range(1, 100) if f(4, i, 0)]))