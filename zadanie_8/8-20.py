'''
Артур составляет 6-буквенные коды перестановкой букв слова АСПЕКТ. При этом нельзя ставить рядом две гласные.
Сколько различных кодов может составить Артур?
'''
from itertools import permutations
words = permutations('аспект')
s = set()
for w in words:
    word = ''.join(w)
    if 'ае' not in word and 'еа' not in word:
        s.add(word)
print(len(s))