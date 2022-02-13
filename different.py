from math import sqrt

start, end = 631632, 684934

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

divs = []
maxDiff = 0
for i in range(start, end+1):
  q = round(sqrt(i))
  D = [2] + list( range(3, q+1, 2) )
  print(D)
  for x in D:
    y = i // x
    if (y - x) <= maxDiff: break
    if i % x == 0 and isPrime(x):
      if x != y and isPrime(y) and (y - x) > maxDiff:
        maxDiff = y - x
        divs = [x, y]
      break

print( divs[0], divs[1] )




