'''
Все 5-буквенные слова, составленные из букв А, О, У, записаны в алфавитном порядке. Вот начало списка:
1. ААААА
2. ААААО

...
Запишите слово, которое стоит на 240-м месте от начала списка.
'''
letters = 'аоу'
s = []
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    s.append(a + b + c + d + e)
print(s[239])