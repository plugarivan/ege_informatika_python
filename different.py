s = [1, 2, 3, 4, 5]
k = 0
for i in range(0, len(s)-1):
    for j in range(i + 1, len(s)):
        k += 1
print(k)