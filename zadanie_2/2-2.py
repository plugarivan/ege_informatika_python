print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x == (not z)) <= ((x or w) == y)) == False:
                    print(x, y, z, w)
