for i in range(1, 1000):
  s = i
  n = 200
  while s // n >= 2:
    s = s + 5
    n = n + 5
  if 99 < s < 1000:
    print(i)




