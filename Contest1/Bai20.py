import math

m, n, a = map(int, input().split())
d = math.ceil(m / a)
r = math.ceil(n / a)  

res = d * r
print(res)
