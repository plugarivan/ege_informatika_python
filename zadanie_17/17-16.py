with open('../files/17/17-10.txt') as f:
    s = [int(x) for x in f]
    numbers = []
    for i in range(1, len(s)):
        