"""
Текстовый файл 24-164.txt состоит не более чем из 106 символов и содержит только заглавные
буквы латинского алфавита (ABC…Z). Текст разбит на строки различной длины. Необходимо найти строку,
содержащую самую длинную цепочку стоящих подряд одинаковых букв. Если таких строк несколько,
надо взять ту, которая в файле встретилась раньше. Определите, какая буква встречается в этой строке реже всего
(но присутствует!). Если таких букв несколько, надо взять ту, которая стоит последней в алфавите.
Запишите в ответе эту букву, а затем – сколько раз она встречается во всем файле.
"""
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open('../files/24/24-164.txt') as f:
    file = f.readlines()
    kmax = 0
    c = []
    for s in file:
        k, ktech = 1, 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                ktech += 1
                if ktech > k:
                    k = ktech
            else:
                ktech = 1
        if k > kmax:
            kmax = k
            min, letMin = 100000, ''
            for letter in alph:
                if s.count(letter) > 0 and s.count(letter) <= min:
                    min = s.count(letter)
                    letMin = letter
    ss = []
    for s in file:
        ss.append(s.count(letMin))

    print(letMin, sum(ss))


