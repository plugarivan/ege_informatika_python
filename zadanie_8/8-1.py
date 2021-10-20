"""
(А. Богданов) Петя составляет пятибуквенные слова перестановкой букв слова МАРТА.
При этом он избегает слов с двумя подряд одинаковыми буквами.
Сколько всего различных слов может составить Петя?
"""
letters = 'марта'
words = set()
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    word = a + b + c + d + e
                    if 'аа' not in word and word.count('м') == 1 and word.count('а') == 2 and word.count('р') == 1 \
                        and word.count('т') == 1:
                        words.add(word)
print(len(words))