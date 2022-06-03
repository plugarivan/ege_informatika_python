'''
Определите, сколько символов * выведет эта процедура при вызове F(35):
Python
def F( n ):
  print("*")
  if n >= 1:
    print("*")
    F(n-1)
    F(n-2)
    print("*")
'''
k = 0
def f(n):
    global k
    k += 1
    if n >= 1:
        k += 1
        f(n - 1)
        f(n - 2)
        k += 1

f(35)
print(k)