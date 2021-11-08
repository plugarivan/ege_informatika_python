'''
(демо-2022) Текстовый файл состоит из символов P, Q, R, S. Определите максимальное количество идущих подряд символов в
прилагаемом файле, среди которых нет идущих подряд символов P.
Для выполнения этого задания следует написать программу
'''
with open('../files/24/24.txt') as f:
    s = f.readline()
    count, maximum = 1, 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1] == 'P':
            count = 1
        else:
            count += 1
            maximum = max(maximum, count)
print(maximum)