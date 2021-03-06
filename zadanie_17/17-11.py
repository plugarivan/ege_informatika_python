'''
В файле 17-205.txt содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения
 от –10 000 до 10 000 включительно. Определите количество пар, в которых хотя бы один из двух элементов заканчивается на 7,
 а их сумма делится на 12. В ответе запишите два числа: сначала количество найденных пар, а затем – максимальную сумму элементов таких пар.
 В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
with open('../files/17/17-205.txt') as f:
    s = [int(x) for x in f]
    res = []
    for i in range(1, len(s)):
        if (abs(s[i]) % 10 == 7 or abs(s[i-1]) % 10 == 7) and (s[i] + s[i-1]) % 12 == 0:
            res.append(s[i] + s[i-1])
print(len(res), max(res))