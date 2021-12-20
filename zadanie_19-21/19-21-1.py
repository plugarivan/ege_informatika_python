'''
'''
#20 задача
def f(x, p):
    if x >= 65 or p > 3:
        if x < 100:
            return p == 3
        else:
            return p == 2
#петя выиграл вторым ходом
    if p % 2:
        return f(x + 1, p + 1) and f(x * 3,  p + 1)
    else:
        return f(x + 1, p + 1) or f(x * 3,  p + 1)

print([i for i in range(1, 100) if f(i, 0)])


#21 задача
def f(x, p):
    if x >= 65 and (p == 4 or p == 2):
        return True
    else:
        if x < 65 and p == 4:
            return False
        else:
            if x >= 65: #перебор камней
                return False
    if p % 2 == 0:
        return f(x + 1, p + 1) and f(x * 3,  p + 1)
    else:
        return f(x + 1, p + 1) or f(x * 3,  p + 1)

print(min([i for i in range(1, 100) if f(i, 0)]))