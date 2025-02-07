def solve(a1, a2, a3, b1, b2, b3, n):
    a = a1 + a2 + a3
    b = b1 + b2 + b3
    na = (a + 4) // 5
    nb = (b + 9) // 10

    if na + nb <= n:
        return True
    return False

if __name__ == '__main__':
    a1, a2, a3, b1, b2, b3 = map(int, input().split())
    n = int(input())

    if solve(a1, a2, a3, b1, b2, b3, n):
        print('YES')
    else:
        print('NO')
