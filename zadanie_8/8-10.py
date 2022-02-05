'''
Из букв слова К А Р К А С составляются 6-буквенные последовательности.
Сколько можно составить различных последовательностей, если известно, что в каждой из них содержится не менее 3 согласных?
'''
import itertools
words = itertools.product('карс', repeat=6)
k = 0
for w in words:
    word = ''.join(w)
    if (word.count('к') +  word.count('р') +  word.count('с')) >= 3:
        k += 1
print(k)
