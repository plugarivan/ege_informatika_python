'''
Артур составляет 5-буквенные коды перестановкой букв слова ВОРОН. При этом нельзя ставить рядом две гласные.
Сколько различных кодов может составить Артур?
'''
from itertools import permutations
words = permutations('ворон')
k = 0
for w in words:
    word = ''.join(w)
    if 'оо' not in word:
        print(word)
        k += 1
print(k)
