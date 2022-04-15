with open('./files/26/26-50.txt') as f:
    n = int(f.readline())
    s = [int(i) for i in f]
    s.sort()
    sred = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            summa = s[i] + s[j]
            if summa % 2 == 0:
                sred.append(summa // 2)
    sred.sort()
    numbers = [x for x in sred if s[n // 2 - 1] < x < s[3 * n // 4]]
print(len(numbers), min(numbers))





