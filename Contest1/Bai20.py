import math
m, n , a = map(int, input().split())

if m % a == 0 and n % a == 0:
    d = m / a
    r = n / a
elif m % a == 0 and n % a != 0:
    d = m / a
    r = math.ceil(n / a)
elif m % a != 0 and n % a == 0:
    d = math.ceil(m / a)
    r = n / a
else:
    d = math.ceil(m / a)
    r = math.ceil(n / a)

res = d * r
print(res)