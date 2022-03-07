import time
tt = time.time()
for i in range(123456789, 223456790):
    divs = set()
    if round(i ** 0.5) == i ** 0.5:
        for d in range(2, round(i ** 0.5) + 1):
            if i % d == 0:
                divs.add(d)
                divs.add(i // d)
                if len(divs) > 3:
                    break

    if len(divs) == 3:
        print(i, max(divs))
print(time.time() - tt)
