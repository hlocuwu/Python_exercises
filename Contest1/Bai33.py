def solve(a, b, c, n):
    if (a + b + c + n) % 3 != 0:
        return False
    coin = (a + b + c + n) / 3
    if coin >= a and coin >= b and coin >= c:
        return True
    return False

if __name__ == '__main__':
    a, b, c, n = map(int, input().split())
    if solve(a, b, c, n):
        print('YES')
    else:
        print('NO')