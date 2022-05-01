def prost(n):
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

k, maximum = 0, 0
for i in range(5555, 7778):
    for d in range(2, round(i ** 0.5)):
        if d * (i // d) == i and prost(d) and prost(i // d) and d % 10 == 3 and (i // d) % 10 == 3:
            maximum = max(maximum, i)
            k += 1
print(maximum, k)
