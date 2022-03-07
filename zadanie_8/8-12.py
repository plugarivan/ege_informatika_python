'''
Ольга составляет 5-буквенные коды из букв О, Л, Ь, Г, А. Каждую букву нужно использовать ровно 1 раз,
при этом Ь нельзя ставить первым и нельзя ставить после гласной. Сколько различных кодов может составить Ольга?
'''
from itertools import permutations
words = permutations('ольга')
k = 0
for w in words:
    word = ''.join(w)
    if word[0] != 'ь' and 'оь' not in word and 'аь' not in word:
        k += 1
print(k)