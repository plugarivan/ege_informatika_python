'''
Пусть M – сумма минимального и максимального натуральных делителей
целого числа, не считая единицы и самого числа. Если таких делителей
у числа нет, то значение M считается равным нулю.
Напишите программу, которая перебирает целые числа, бо́льшие 700 000,
в порядке возрастания и ищет среди них такие, для которых значение M
оканчивается на 8. Выведите первые пять найденных чисел
и соответствующие им значения M.
Формат вывода: для каждого из пяти таких найденных чисел в отдельной
строке сначала выводится само число, затем – значение М.
Строки выводятся в порядке возрастания найденных чисел.
Количество строк в таблице для ответа избыточно.
'''
for i in range(700001, 700500):
    divs = set()
    for d in range(2, round(i ** 0.5)):
        if i % d == 0:
            divs.update((d, i//d))
    if len(divs) > 0:
        m = max(divs) + min(divs)
        if m % 10 == 8:
            print(i, m)