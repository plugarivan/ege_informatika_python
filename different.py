letters = 'елмур'
k = []
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                k.append(a+b+c+d)
print(k.index('леее')+1)