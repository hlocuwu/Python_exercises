def solve(n):
    for i in range(1, n + 1):
        print('*' * i)
    print()

    for i in range(n ,0 , -1):
        print('*' * i)
    print()

    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * i)
    print()

    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * i)
    print()

    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * (i + 1))
        else:
            print('*' + ' ' * (i - 1) + '*')
            
    
if __name__ == "__main__":
    n = int(input())
    solve(n)