"""
Дана программа для исполнителя Редактор:
НАЧАЛО
  ПОКА нашлось (111)
    заменить (111, 2)
    заменить (222, 1)
  КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой программы к строке вида 1…12…2 (2018 единиц и 2019 двоек)?
"""
s = 2018 * '1' + 2019 * '1'
while '111' in s:
    s = s.replace('111', '2', 1)
    s = s.replace('222', '1', 1)
print(s)