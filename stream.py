def prost(n):
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


minimum = 1000000000000
for i in range(309829, 365875):
    for d in range(2, round(i ** 0.5)):
        if d * (i // d) == i and prost(d) and prost(i // d):
            print(d, i // d)
            if abs(i // d - d) < minimum:
                minimum = abs(i // d - d)
                d1, d2 = d, i // d
print(minimum, d1, d2)

