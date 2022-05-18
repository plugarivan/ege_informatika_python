'''
Петя составляет шестибуквенные слова перестановкой букв слова АДЖИКА. При этом он избегает слов с двумя подряд одинаковыми буквами.
Сколько всего различных слов может составить Петя?
'''
from itertools import permutations
k = set()
words = permutations('аджика')
for w in words:
    word = ''.join(w)
    if 'аа' not in word:
        k.add(word)
print(len(k))