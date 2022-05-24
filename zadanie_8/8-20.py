'''
Артур составляет 5-буквенные коды перестановкой букв слова АРЕАЛ. При этом нельзя ставить рядом две гласные.
Сколько различных кодов может составить Артур?
'''
from itertools import permutations
words = permutations('ареал')
s = set()
for w in words:
    word = ''.join(w)
    if 'аа' not in word and 'ае' not in word and 'еа' not in word:
        s.add(word)
print(len(s))