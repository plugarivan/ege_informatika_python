print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (x and (y and z or y and (not(w)) or (not(z)) and (not(w)))) == True:
                    print(x, y, z, w)

                    #ywzx