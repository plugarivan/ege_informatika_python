import random

s = [random.randrange(1, 101) for i in range(1, 101)]
for i in range(1, len(s)):
    if s[i] > s[i-1] and s[i] > s[i+1]



