'''

'''
fib = [1]*10
for i in range(10):
    if i > 1:
        fib[i] = fib[i-2] + fib[i-1]
print(fib)
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    for c in fib:
        if c >= x:
            return f(x + 1, y) + f(x + 5, y) + f(x + c, y)


print(f(1, 13))