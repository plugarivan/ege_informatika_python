for a in range(1, 60):
    for b in range(1, 60):
        for c in range(1, 60):
            s = '0' + a * '1' + b * '2' + c * '3'
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '2302', 1)
                s = s.replace('02', '10', 1)
                s = s.replace('03', '201', 1)
            if s.count('1') == 51 and s.count('2') == 29 and s.count('3') == 23:
                print(c)