for m in range(2, 1000, 2):
    for n in range(1, 1001, 2):
        if 100000000<2**m * 7**n<300000000:
            print(2**m * 7**n, m +n)