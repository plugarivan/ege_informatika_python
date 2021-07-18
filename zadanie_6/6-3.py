"""
(А.Г. Минак) Определите, при каком наименьшем введённом значении переменной s программа выведет число,
не меньшее, чем 30.
Python
s = int(input())
n = 32
while n > s:
  s = s + 1
  n = n - 1
print(n)
"""
for i in range(1, 1000):
    s = i
    n = 32
    while n > s:
        s = s + 1
        n = n - 1
    if n >= 30:
        print(i)
        break