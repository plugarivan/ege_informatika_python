k = set()
for n in range(4, 10000):
    s = bin(n)[2:]
    if s.count('1') > s.count('0'):
        s += '0'
    else:
        s += '1'
    if len(s) % 2 == 0:
        s = s[:((len(s) - 1) // 2)] + s[len(s) // 2 + 1:]
    else:
        s = s[:(len(s) // 2) - 1] + s[len(s) // 2 + 2:]
    if 50 <= int(s, 2) <= 100:
        k.add(int(s, 2))
print(len(k))

