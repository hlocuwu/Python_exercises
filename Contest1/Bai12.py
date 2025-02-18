t, n = map(int, input().split())

if (t > 0 and t < 13 and n > 0):
    if (t in {1, 3, 5, 7, 8, 10, 12}):
        print(31)
    elif (t in {4, 6, 9, 11}):
        print(30)
    else:
        if (n % 400 == 0 or (n % 100 != 0 and n % 4 == 0)):
            print(29)
        else:
            print(28)
else:
    print('INVALID')
    