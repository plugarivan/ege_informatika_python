'''
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1. Строится двоичная запись числа N.
2. К этой записи дописываются справа ещё два разряда по следующему правилу:
а) складываются все цифры двоичной записи, и остаток от деления суммы на 2 дописывается в конец числа (справа). Например, запись 11100 преобразуется в запись 111001;
б) над этой записью производятся те же действия – справа дописывается остаток от деления суммы цифр на 2.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N) является двоичной записью искомого числа R.
Укажите такое наименьшее число N, для которого результат работы алгоритма больше 137. В ответе это число запишите в десятичной системе счисления.
'''
for n in range(1, 1000):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'
    if int(s, 2) > 137:
        print(n)
        break
