maximum_divs = 0
for i in range(286564, 287271):
    divs = set()
    for d in range(1, round(i ** 0.5) + 1):
        if i % d == 0:
            divs.add(d)
            divs.add(i // d)
    maximum_divs = max(len(divs), maximum_divs)
print(maximum_divs)

for i in range(286564, 287271):
    divs = set()
    for d in range(1, round(i ** 0.5) + 1):
        if i % d == 0:
            divs.add(d)
            divs.add(i // d)
    if len(divs) == maximum_divs:
        print(i, sorted(list(divs), reverse=True))

#112 143520