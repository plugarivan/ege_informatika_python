"""
На вход программы поступает последовательность из целых положительных чисел.
Необходимо выбрать такую подпоследовательность подряд идущих чисел, чтобы их сумма была максимальной
и делилась на 89, а также её длину.
Если таких подпоследовательностей несколько, выбрать такую, у которой длина меньше.
"""
with open('../files/27/27_A.txt') as f:
    n = int(f.readline())
    s = [int(i) for i in f]
    maxsum, minlen = 0, 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            summa = sum(s[i:j+1])
            if summa % 89 == 0:
                if summa > maxsum:
                    maxsum = summa
                    minlen = j - i + 1
                if summa == maxsum:
                    minlen = min(minlen, j - i + 1)
    print(minlen)

