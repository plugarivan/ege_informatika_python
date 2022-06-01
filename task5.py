k = 0
for n in range(300, 401):
    s = sorted(str(n))
    if s[0] == '0':
        if s[1] == '0':
            mx = mn = int(s[2] + '0')
        else:
            mn = int(s[1] + '0')
            mx = int(s[2] + s[1])
    else:
        mn = int(s[0] + s[1])
        mx = int(s[2] + s[1])
    if mx - mn == 20:
        k += 1
print(k)




