with open('./files/26/26-45.txt') as f:
    n = int(f.readline())
    s = [int(i) for i in f]
    slovar = dict(zip(s, [0 for t in range(n)]))
    ss = []
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if (s[i] + s[j]) % 2 == 0 and (s[i] + s[j]) // 2 in s:
                ss.append((s[i] + s[j]) // 2)
print(len(ss), max(ss))

