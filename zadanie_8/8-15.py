'''Артур составляет 6-буквенные коды перестановкой букв слова ВОРОТА. При этом нельзя ставить рядом две гласные.
Сколько различных кодов может составить Артур?'''
letters = 'ворота'
s = set()
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    for f in letters:
                        word = a + b + c + d + e + f
                        if word.count('в') == 1 and word.count('о') == 2 and word.count('р') == 1 and word.count('т') == 1 and \
                                word.count('а') == 1 and 'оо' not in word and 'оа' not in word and 'ао' not in word:
                            s.add(word)
print(len(s))