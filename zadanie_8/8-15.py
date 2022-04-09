'''
Миша составляет 5-буквенные коды из букв С, А, К, У, Р, А.
Каждая допустимая гласная буква может входить в код не более одного раза. Сколько кодов может составить Миша?
'''
letters = 'сакур'
k = 0
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    word = a + b + c + d + e
                    if word.count('а') <= 1 and word.count('у') <= 1:
                        k += 1
print(k)