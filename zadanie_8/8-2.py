'''
Найдите количество 9-значных чисел таких, что в их десятичной записи ровно 7 цифр "8" и нет цифр "1" и "2"
'''

count = 0
for i in range(308888888, 888888899):
    if str(i).count('8') == 7 and '1' not in str(i) and '2' not in str(i):
        print(i)
        count += 1
print(count)
