a, b = map(int, input().split())

res1 = a // b * b

if a % b == 0:
    res2 = a
else:
    res2 = (a // b + 1) * b

print(res1, res2)