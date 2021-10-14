summa = 0
a = int(input())
while a != 0:
    if a % 7 == 0 and a % 10 == 2:
        summa += a
    a = int(input())
print(summa)

