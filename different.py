i = 550001
k = 0
while k != 5:
    divs = set()
    for d in range(2, round(i ** 0.5)+1):
        if i % d == 0:
            divs.add(d)
            divs.add(i // d)
    if len(divs) != 0:
        if (sum(divs) // len(divs)) % 31 == 13:
            k += 1
            print(i, sum(divs) // len(divs))
    i += 1



