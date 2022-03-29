'''
(А. Куканова) Лиля составляет 5-буквенные слова из букв С, О, Т, К, А, П, Л, З. Слово не должно заканчиваться на гласную
и содержать сочетания ЗЛО. Буквы в слове не повторяются. Сколько слов может составить Лиля?
'''
from itertools import product
words = product('соткаплз', repeat=5)
k = 0
for w in words:
    word = ''.join(w)
    if 'зло' not in word and word[-1] not in 'оа' and word.count('с') <= 1 and word.count('о') <= 1 and word.count('т') <= 1 and \
            word.count('к') <= 1 and word.count('а') <= 1 and word.count('п') <= 1 and word.count('л') <= 1 and word.count('з') <= 1:
        k += 1
print(k)