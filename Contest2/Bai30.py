def solve(n):
    for i in range(n):
        m = int(input())
        if m % 2 == 0:
            print('EVEN')
        else:
            print('ODD')

if __name__ == '__main__':
    n = int(input())
    solve(n)