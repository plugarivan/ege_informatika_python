from math import sqrt
for i in range(190061, 190073):
    divs = set()
    for d in range(1, round(sqrt(i)) + 1):
        if i % d == 0 and d % 2 != 0:
            divs.add(d)
            if i // d % 2 != 0:
                divs.add(i // d)
    if len(divs) == 4:
        print(sorted(divs))