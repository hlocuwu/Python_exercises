def solve(a, b, n):
    for x in range (int(n // a + 1)):
        if (n - a * x) % b == 0:
            return True
    return False

if __name__ == '__main__':
    a, b, n =   map(int, input().split())
    if (solve(a, b, n)):
        print('YES')
    else:
        print('NO')