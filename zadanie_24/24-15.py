"""
Определите символ, который чаще всего встречается в файле после двух одинаковых символов
"""
with open('../files/24/s24.txt') as f:
    s = f.readline()
    letters = {}
    for i in range(2, len(s) - 1):
        if s[i - 1] == s[i - 2]:
            key = s[i]
            letters[key] = letters.get(key, 0) + 1 #Метод get() возвращает значение по указанному ключу в параметрах.
    Max = max(letters.values())
    for x in letters.items():
        if x[1] == Max:
            print(x[0])
