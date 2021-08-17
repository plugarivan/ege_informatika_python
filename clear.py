for i in range(0, 256):
    x = str(bin(i-1))[2:]
    if len(x) < 8:
        x = (8-len(x)) * '0' + x
    x1 = ''
    for s in x:
        if s == '0':
            x1 += '1'
        else:
            x1 += '0'
    if x1[-1] == '0':
        f = x1[:-1] + '1'
    print(x1[:-1] + '1')
    if int(f, 2) == 221:
        print(i)

"""
11011101
00100010
"""