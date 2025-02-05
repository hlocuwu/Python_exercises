N = int(input())
if N % 2 == 0:
    print('YES')
else:
    print('NO')
if N % 3 == 0 and N % 5 == 0:
    print('YES')
else:
    print('NO')
if N % 3 == 0 and N % 7 != 0:
    print('YES')
else:
    print('NO')
if N % 3 == 0 or N % 7 == 0:
    print('YES')
else:
    print('NO')
if N > 30 and N < 50:
    print('YES')
else:
    print('NO')
if N >= 30 and (N % 2 == 0 or N % 3 == 0 or N % 5 == 0):
    print('YES')
else:
    print('NO')
if N > 10 and N < 99:
    if N % 10 in {2, 3, 5, 7}:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
if N <= 100 and N % 23 == 0:
    print('YES')
else:
    print('NO')
if N < 10 or N > 20:
    print('YES')
else:
    print('NO')
if (N % 10) % 3 == 0:
    print('YES')
else:
    print('NO')