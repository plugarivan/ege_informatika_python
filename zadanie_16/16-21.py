'''
Определите, сколько символов * выведет эта процедура при вызове F(28):
Python
def F( n ):
  print("*")
  if n >= 1:
    print("*")
    F(n-1)
    F(n-2)
'''
k = 0
def f(n):
    global k
    k += 1
    if n >= 1:
        k += 1
        f(n - 1)
        f(n - 2)

f(28)
print(k)