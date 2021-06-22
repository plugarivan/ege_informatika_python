"""
Петя составляет шестибуквенные слова перестановкой букв слова АВРОРА.
При этом он избегает слов с двумя подряд одинаковыми буквами.
Сколько всего различных слов может составить Петя?
"""
letters = 'АВРОРА'
mn = set()
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    for f in letters:
                        word = a + b + c + d + e + f
                        if word.count('А') == 2 and word.count('Р') == 2 and word.count('В') == 1 and word.count('О') == 1 and 'АА' not in word and 'РР' not in word:
                            mn.add(word)
print(len(mn))





