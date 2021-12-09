data = [int(x) for x in open('../files/17/17-243.txt')]

def sumDigits( n ):
  return sum( map(int, str(n)) )

ref = sum( sumDigits(x) for x in data
                          if x % 49 == 0 )
print( ref )

def nCond2( arr, func, func2 ):
  return (func(arr[0]) and not func(arr[1]) and func2(arr[1]) or
          func(arr[1]) and not func(arr[0]) and func2(arr[0]))

count, mi, ma = 0, 10**10, 0
for i, n in enumerate(data):
   if i > 0:
     pair = data[i-1:i+1]
     if nCond2( pair, lambda x: x > ref,
                      lambda x: x % 10 == 7 ):
        # print(pair)
        ma = max( ma, sum(pair) )
        mi = min( mi, sum(pair) )
        count += 1

print( count, mi )
print( count, ma )