'''

'''
i = 800001
k = 0
while k != 5:
    divs = set()
    for d in range(2, round(i ** 0.5)):
        if i % d == 0:
            divs.add(d)
            divs.add(i // d)
    if len(divs) != 0:
        if (max(divs) + min(divs)) % 138 == 0:
            k += 1
            print(i, max(divs) + min(divs))
    i += 1