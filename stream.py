s = 50 * '1' + 50 * '2' + 50 * '3'
while '21' in s or '31' in s or '23' in s:
    if '21' in s:
        s = s.replace('21', '12', 1)
    if '31' in s:
        s = s.replace('31', '13', 1)
    if '23' in s:
        s = s.replace('23', '32', 1)
print(s[10] + s[90] + s[130])
