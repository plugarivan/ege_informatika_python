'''
(Крылов) Сколько существует различных четырёхзначных чисел, записанных в десятичной системе счисления в записи которых есть ровно
две одинаковые цифры, причм стоящие рядом?
'''
from itertools import product
words = product('0123456789', repeat=4) #i -это количество символов в слове
k = 0
for w in words:
    word = ''.join(w)
    if word[0] != '0' and ((word[0] == word[1] and word.count(word[0]) == 2) or (word[1] == word[2] and word.count(word[1]) == 2) or (word[2] == word[3] and word.count(word[2]) == 2)):
        k += 1
print(k)