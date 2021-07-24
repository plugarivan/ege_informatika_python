for i in range(100, 10000):
    x = i
    l = x - 30
    m = x + 30
    while l != m:
        if l > m:
            l = l - m
        else:
            m = m - l
    if m == 30:
        print(i)
        break