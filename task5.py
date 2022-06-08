s = '111010111'

if len(s) % 2 == 0:
    s = s[:((len(s)-1) // 2)] + s[len(s) // 2 + 1:]
else:
    s = s[:(len(s) // 2) - 1] + s[len(s) // 2 + 2:]



