'''
Укажите наименьшее целое значение А, при котором выражение
(3y + x < A) ∨ (x > 12) ∨ (y > 15)
истинно для любых целых положительных значений x и y.
'''
def f(x, y, a):
    return (3 * y + x < a) or (x > 12) or (y > 15)

for a in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not(f(x, y, a)):
                flag = False
                break
        if not(flag):
            break
    if flag:
        print(a)
        break
