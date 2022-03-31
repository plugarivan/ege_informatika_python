for i in range(62, 10000):
    x = i
    a = x - 61
    b = 3 * x - 138
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    if a == 45:
        print(i)
        break