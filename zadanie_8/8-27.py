'''
(А.М. Кабанов) Алексей составляет 5-буквенные слова из букв М, А, Г, И, С, Т, Р. Каждую букву можно использовать не более
одного раза, при этом в слове нельзя использовать более одной гласной. Сколько различных кодов может составить Алексей?
'''
from itertools import product
words = product('магистр', repeat=5)
k = 0
for w in words:
    word = ''.join(w)
    if (word.count('а') + word.count('и')) <= 1 and word.count('м') <= 1 and word.count('а') <= 1 \
            and word.count('г') <= 1 and word.count('и') <= 1 and word.count('с') <= 1 and word.count('т') <= 1 and word.count('р') <= 1:
        k += 1
print(k)