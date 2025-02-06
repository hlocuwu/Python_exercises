n, a, b = map(int, input().split())

pa = a
pb = b / 2

if n % 2 == 0:
    if pa > pb:
        res = int(n * pb)
    else:
        res = n * pa
else:
    if pa > pb:
        res = int((n - 1) * pb + pa)
    else:
        res = n * pa

print(res)