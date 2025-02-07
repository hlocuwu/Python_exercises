import math

a = float(input())
max = math.ceil(a)
min = math.floor(a)
 
if max - a > a - min:
    res = min
elif max - a < a - min:
    res = max
else:
    res = max

print(res)