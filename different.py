for n in range(1, 256):
    s = bin(n)[2:]
    if len(s) < 8:
        s = (8 - len(s)) * '0' + s
    s1 = ''
    for x in s:
        if x == '1':
            s1 += '0'
        else:
            s1 += '1'
    if int(s1, 2) - n == 45:
        print(n)