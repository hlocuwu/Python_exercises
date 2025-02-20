def solve(n):
    for i in range(n):
        print('*' * n)
    print()

    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' '*(n - 2) + '*')
    print()

    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + '#'*(n - 2) + '*')
    print()

    for i in range(1, n + 1):
        if i == 1 or i == n:
            print(f'{i} ' * n)
        else:
            print(f'{i} ' + ' ' * (2 * (n - 2)) + f'{i}')
    
if __name__ == "__main__":
    n = int(input())
    solve(n)