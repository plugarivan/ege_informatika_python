def f(x):
    yield x ** 2

def ff(x):
    return x ** 2

for i in f(10):
    print(i)
print(ff(5))