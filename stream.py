'''
2 ** n * p ** 4
'''

def prost(n):
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

for n in range(105000000, 115000001):
    x = n
    while x % 2 == 0:
        x //= 2
    sqrt4 = round(x ** 0.25)
    if prost(sqrt4) and sqrt4 ** 4 == x:
        print(n, x)