'''
(Д.Ф. Муфаззалов, г. Уфа) Определите количество простых чисел в диапазоне [2; 200000]
'''

def prost(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

k = 0
for i in range(2, 200001):
    if prost(i):
        k += 1
print(k)