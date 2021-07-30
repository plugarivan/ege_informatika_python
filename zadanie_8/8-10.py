"""
Андрей составляет 6-буквенные коды из букв А, Н, Д, Р, Е, Й. Буква А должна входить в код не менее одного раза,
а буква Й - не более одного раза. Сколько различных кодов может составить Андрей?
"""
letters = 'андрей'
k = 0
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    for f in letters:
                        word = a + b + c + d + e + f
                        if word.count('а') >= 1 and word.count('й') <= 1:
                            k += 1
print(k)