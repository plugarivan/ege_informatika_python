'''
На числовой прямой даны два отрезка: D = [17;58] и C = [29;80]. Укажите наименьшую возможную длину такого отрезка A,
для которого логическое выражение истинно при любом значениии переменной x.
'''
def f(x, a1, a2):
    return (17 <= x <= 58) <= ((not(29 <= x <= 80) and not(a1 <= x < a2)) <= (not(17 <= x <= 58)))

s = []
for a1 in range(-100, 100):
    for a2 in range(-100, 100):
        answer = True
        for x in range(-100, 100):
            if not(f(x, a1, a2)):
                answer = False
                break
        if answer:
            s.append(a2 - a1)
print(min(s))

