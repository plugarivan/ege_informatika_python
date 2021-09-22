'''
Лена составляет 5-буквенные слова из букв Я, С, Н, О, В, И, Д, Е, Ц, причём слово должно начинаться с согласной и
заканчиваться гласной. Первая и последняя буквы слова встречаются в нем только один раз;
остальные буквы могут повторяться. Сколько слов может составить Лена?
'''
letters = 'ясновидец'
k = 0
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    word = a + b + c + d + e
                    if word[0] in 'снвдц' and word[-1] in 'яоие' and word.count(word[0]) == 1 and word.count(word[-1]) == 1:
                        k += 1
print(k)