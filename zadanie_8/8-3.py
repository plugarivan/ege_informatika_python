"""
Маша составляет 6-буквенные коды из букв Р, У, Л, Ь, К, А. Каждую букву нужно использовать ровно 1 раз,
при этом буква Ь не может стоять на первом месте и после гласной. Сколько различных кодов может составить Маша?
"""
letters = 'РУЛЬКА'
k = 0
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    for f in letters:
                        word = a + b + c + d + e + f
                        if word.count('Р') == 1 and word.count('У') == 1 and word.count('Л') == 1 and \
                                word.count('Ь') == 1 and word.count('К') == 1 and word.count('А') == 1 and \
                            word[0] != 'Ь' and 'УЬ' not in word and 'АЬ' not in word:
                            k += 1
print(k)