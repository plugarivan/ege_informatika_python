'''
(А. Куканова) Маша составляет четырёхбуквенные слова из букв A, B, C, D, E, причём сначала в слове должны быть
расположены гласные в алфавитном порядке, затем согласные в обратном алфавитном порядке. Буквы могут повторяться.
Слово может состоять только из гласных или только из согласных. Пример подходящего слова: AEDC. Сколько различных слов может составить Маша?
'''
k = 0
letters = 'aedcb'
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                word = a + b + c + d
                if word.count('ea') == 0 and word.count('de') == 0 and word.count('cd') == 0 and word.count('bc') == 0 and word.count(
                        'da') == 0 and word.count('bd') == 0 and word.count('ce') == 0 and word.count('ca') == 0 and word.count(
                        'be') == 0 and word.count('ba') == 0:
                    k += 1
print(k)


