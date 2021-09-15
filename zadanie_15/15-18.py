'''
Укажите наименьшее целое значение А, при котором выражение
(y + 2x < A) ∨ (x > 20) ∨ (y > 30)

истинно для любых целых положительных значений x и y.
'''

for a in range(1, 100):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not((y + 2 * x < a) or (x > 20) or (y > 30)):
                flag = False
                break
        if not(flag):
            break
    if flag:
        print(a)
        break

