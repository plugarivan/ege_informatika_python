'''

'''
with open('../files/24/24.txt') as f:
    s = f.readline()
    maximum = 1
    while 'PP' in s:
        s = s.replace('PP', 'P P', 1)
        maximum = max(maximum, s.count(' '))
print(maximum)

