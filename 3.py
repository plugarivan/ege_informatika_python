minimum = 30001
k = int(input())
for i in range(1, k + 1):
    a = int(input())
    if a % 3 == 0:
        if a < minimum:
            minimum = a
print(minimum)