def solve(a, b, n):
    for x in range (int(n / a)):
        for y in range (int(n / b)):
            if a * x + b * y == n:
                return True
    return False

if __name__ == '__main__':
    a, b, n =   map(int, input().split())
    if (solve(a, b, n)):
        print('YES')
    else:
        print('NO')