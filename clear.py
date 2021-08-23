
s = '>' + 14 * '1' + 20 * '2' + 25 * '3'

while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>3', 1)
    if '>2' in s:
        s = s.replace('>2', '2>', 1)
    if '>3' in s:
        s = s.replace('>3', '11>2', 1)

sum = 0
for i in s:
    if i != '>':
        sum += int(i)
print(sum)