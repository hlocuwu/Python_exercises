a, b, c = map(int, input().split())

if a > 0 and b > 0 and c > 0 and (a + b > c or a + c > b or b + c > a):
    print('TRUE')
else:
    print('FALSE')