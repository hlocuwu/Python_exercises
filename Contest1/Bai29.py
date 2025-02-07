def solve(a, b, c, d):
    if a == 0 or b == 0 or c == 0:
        return False
    if b % a == 0 and c % b == 0 and d % c == 0:
        r1 = b // a
        r2 = c // b
        r3 = d // c
        return r1 == r2 == r3
    return False

if __name__ == '__main__':
    a, b, c, d = map(int, input().split())
    if solve(a, b, c, d):
        print('YES')
    else:
        print('NO')