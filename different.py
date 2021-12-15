with open('../ege_informatika_python/files/26/26-s1.txt') as f:
    data = f.readlines()
    del data[0]
    data = list(map(int, data))
    b = [x for x in data if x <= 200]  # те на которые скидка не предоставляется
    c = [x for x in data if x > 200]  # те на которые будем делать скидку
    c.sort()
    d = c[:len(c) // 2]  # товары на которые будет скидка
    c = c[len(c) // 2:]
    print(sum(b) + sum(c) + 0.7 * sum(d))
    print(max(d))






