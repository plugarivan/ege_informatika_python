def f(a1, a2, x):
    return ((a1 <= x < a2) or (10 <= x <= 40)) or ((5 <= x <= 15) <= (35 <= x <= 50))

s = []
for a1 in range(-100, 100):
    for a2 in range(-100, 100):
        flag = True
        for x in range(-100, 100):
            if not(f(a1, a2, x)):
                flag = False
                break
        if flag:
            s.append(a2 - a1)
print(min(s))
