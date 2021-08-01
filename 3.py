from random import randint

a = [randint(0, 10) for i in range(10)]
print(a)

b = a.index(max(a))
c = a.index(min(a))
a[b], a[c] = a[c], a[b]
print(a)


