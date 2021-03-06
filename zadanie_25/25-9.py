'''
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [4301614; 4301717], простые числа.
Выведите все найденные простые числа в порядке возрастания, слева от каждого числа выведите его номер по порядку.
'''
def prost(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(4301614, 4301718):
    if prost(i):
        print(i)