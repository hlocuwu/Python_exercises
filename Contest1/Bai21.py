a, b, k = map(int, input().split())

t = (k + 1) // 2
p = k // 2

res = t * a - p * b
print(res)