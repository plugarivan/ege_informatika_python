'''
Текстовый файл 24-164.txt состоит не более чем из 106 символов и содержит только заглавные буквы латинского алфавита (ABC…Z).
Текст разбит на строки различной длины. В строках, содержащих менее 15 букв G, нужно определить и вывести максимальное расстояние между одинаковыми буквами в одной строке.
'''
with open('../files/24/24-164.txt') as f:
    maximum = 0
    for s in f:
        if s.count('G') < 15:
            slovar = {}
            for c in s:
                slovar[c] = slovar.get(c, 0) + 1
            for i in slovar.keys():
                maximum = max(maximum, s.rindex(i)-s.index(i))
print(maximum)
