'''
Исполнитель Чертёжник перемещается на координатной плоскости, оставляя след в виде линии.
Чертёжник может выполнять команду Сместиться на (a, b) (где a, b – целые числа),
перемещающую Чертёжника из точки с координатами (x, y) в точку с координатами (x + a, y + b).
Чертёжнику был дан для исполнения следующий алгоритм:

Сместиться на (16, -21)
Повтори N раз
  Сместиться на (a, b)
  Сместиться на (-1, -2)
конец
Сместиться на (-60, -12)
После выполнения этого алгоритма Чертёжник возвращается в исходную точку.
Какое наибольшее число повторений могло быть указано в конструкции «Повтори … раз»?
'''
for n in range(1, 100):
    for a in range(-100, 100):
        for b in range(-100, 100):
            if (16 + n * (a - 1) - 60) == (-21 + n * (b - 2) - 12) == 0:
                print(n)