def nFun(a, func):
    return [func(k) for k in a].count(True)

with open('../files/17/17-1.txt') as f:
    s = [int(x) for x in f]
    sred = sum(s) // len(s)
    numbers = []
    for i in range(len(s) - 2):
        tr = s[i:i + 3]
        if nFun(tr, lambda x: x < sred) >= 2 and nFun(tr, lambda x: '1' in str(x)) == 3:
            numbers.append(sum(tr))
print(len(numbers), max(numbers))





