'''
(А. Кабанов) В файле 17-3.txt содержится последовательность целых чисел. Элементы последовательности могут принимать
целые значения от -10 000 до 10 000 включительно. Определите и запишите в ответе сначала количество пар элементов
последовательности, произведение которых положительно, а сумма кратна 7, затем минимальное из произведений элементов
таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
with open('../files/17/17-3.txt') as f:
    s = [int(x) for x in f]
    numbers = []
    for i in range(1, len(s)):
        if (s[i] * s[i - 1]) > 0 and (s[i] + s[i - 1]) % 7 == 0:
            numbers.append(s[i] * s[i - 1])
print(len(numbers), min(numbers))
