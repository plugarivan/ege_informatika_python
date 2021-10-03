'''
Дана программа для исполнителя Редактор:
НАЧАЛО
  ПОКА нашлось (53)
    заменить (53, 8)
  КОНЕЦ ПОКА
КОНЕЦ
Исходная строка содержит 11 троек и некоторое количество пятерок, других цифр нет, точный порядок расположения
троек и пятерок неизвестен. После выполнения программы получилась строка с суммой цифр 118.
Какое наименьшее количество пятерок могло быть в исходной строке?
'''
for n in range(1, 20):
    s = n * '5' + 11 * '3'
    while '53' in s:
        s = s.replace('53', '8', 1)
    if sum(map(int, list(s))) == 118:
        print(n)
        break