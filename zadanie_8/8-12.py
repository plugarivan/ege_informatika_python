"""
Все 5-буквенные слова, составленные из букв С, Л, О, Н записаны в алфавитном порядке и пронумерованы.
Запишите слово, которое стоит под номером 1020
"""
letters = 'ЛНОС'
s = []
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    s.append(a + b + c + d + e)
print(s[1021])