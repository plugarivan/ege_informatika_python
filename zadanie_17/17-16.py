with open('../files/17/17-10.txt') as f:
    s = [int(x) for x in f]
    numbers = []
    for i in range(1, len(s)):
        summa = s[i] + s[i - 1]
        ch = 0
        while summa > 0:
            ch += summa % 7
            summa //= 7
        f = str(ch)
        if f == f[::-1]:
            fff = int(f, 7)
            numbers.append(fff)
print(numbers)