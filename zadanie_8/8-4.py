'''
Артур составляет 5-буквенные коды перестановкой букв слова ВОРОН. При этом нельзя ставить рядом две гласные.
Сколько различных кодов может составить Артур?
'''
from itertools import permutations
words = permutations('ворон')
s = set()
for w in words:
    word = ''.join(w)
    if 'оо' not in word:
        s.add(word)
print(len(s))
