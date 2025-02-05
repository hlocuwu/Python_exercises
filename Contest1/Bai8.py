a, b = map(int, input().split())

tong = a + b
hieu = a - b
tich = a * b

if b != 0:
    thuong = a / b
    print(tong, hieu, tich,'%.4f' % thuong, sep = '\n')
else:
    thuong = 'INVALID'
    print(tong, hieu, tich, thuong, sep = '\n')