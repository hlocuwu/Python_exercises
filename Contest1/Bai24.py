d1, d2, d3 = map(int, input().split())

res1 = d1 + d3 + d2
res2 = d1 + d1 + d2 + d2
res3 = d1 + d3 + d3 + d1
res4 = d2 + d3 + d3 + d2

res = min({res1, res2, res3, res4})

print(res)