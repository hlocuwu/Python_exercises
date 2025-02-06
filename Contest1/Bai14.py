a, b, c, d = map(float, input().split())

avg = (a + b + c * 2 + d * 3) / 7

if avg >= 8:
    print('GIOI')
elif avg >= 6.5:
    print('KHA')
elif avg >= 5:
    print('TRUNG BINH')
else:
    print('YEU')