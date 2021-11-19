print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x and y) or (y and z)) == ((x <= w) and (w <= z)):
                    print(x, y, z, w)
