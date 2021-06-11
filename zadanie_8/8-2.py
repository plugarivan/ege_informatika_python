"""
Все 5-буквенные слова, составленные из 5 букв А, К, Л, О, Ш, записаны в алфавитном порядке. Вот начало списка:
1. ААААА
2. ААААК
3. ААААЛ
4. ААААО
5. ААААШ
6. АААКА
...
На каком месте от начала списка стоит слово ШКОЛА?
"""
letters = 'АКЛОШ'
s = []
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    word = a + b + c + d + e
                    s.append(word)
print(s.index('ШКОЛА')+1)