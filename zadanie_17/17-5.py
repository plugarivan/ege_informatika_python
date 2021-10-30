'''

'''
with open('../files/17/17-4.txt') as f:
    s = [int(x) for x in f]
    numbers = []
    for i in s:
        if bin(i)[-5:-1] == '1001' and i % 5 == 1 and i // 5 % 5 == 1:
            numbers.append(i)
    print(max(numbers), sum(numbers))