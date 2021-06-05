for i in range(1, 1000):
    s = i
    n = 400
    while s - n > 0:
        s = s - 20
        n = n - 15
    if s < 0:
        print(i)
        break