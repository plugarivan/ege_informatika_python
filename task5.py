days = int(input())
count, summa, yes = 0, 0, 0
for i in range(days):
    temp = int(input())
    summa += temp
    count += 1
    if temp > 0:
        yes += 1
if yes >= 5:
    print(summa / count)
    print('YES')
else:
    print(summa / count)
    print('NO')



