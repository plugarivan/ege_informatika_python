with open('./files/24/24-2.txt') as f:
    s = f.readline()
    k, kmax = 1, 1
    maxi = 0
    for i in range(1, len(s)):
        if s[i] < s[i - 1]:
            k += 1
            if k > kmax:
                kmax = k
                maxi = i
        else:
            k = 1
print(maxi - kmax + 1 + 1)
