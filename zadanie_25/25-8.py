for i in range(1, 100):
    s = (i + 1) // 7
    n = 36
    while s < 2050:
        s = s * 2
        n = n + 3
    if n == 66:
        print(i)

