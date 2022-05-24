'''
Вася составляет слова из букв слова АВТОРОТА. Код должен состоять из 8 букв, и каждая буква в нём должна встречаться
столько же раз, сколько в заданном слове. Кроме того, в коде не должны стоять рядом две гласные и две согласные буквы.
Сколько различных слов может составить Вася?
'''
from itertools import permutations
words = permutations('авторота')
k = set()
for w in words:
    word = ''.join(w)
    if 'оо' not in word and 'аа' not in word and 'ао' not in word and 'оа' not in word:
        k.add(word)
print(len(k))