for n in range(1, 100):
    s = bin(n)[2:]
    if s.count('1') == s.count('0'):
        s += s[-1]
    elif s.count('1') > s.count('0'):
        s += '0'
    else:
        s += '1'
    if s.count('1') == s.count('0'):
        s += s[-1]
    elif s.count('1') > s.count('0'):
        s += '0'
    else:
        s += '1'
    if s.count('1') == s.count('0'):
        s += s[-1]
    elif s.count('1') > s.count('0'):
        s += '0'
    else:
        s += '1'
    if int(s, 2) % 4 == 0:
        print(n)
