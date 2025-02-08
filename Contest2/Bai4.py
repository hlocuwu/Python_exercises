def solve(n):
    s = 0
    for i in range(1, n + 1):
        s += 1 / i
    return s

if __name__ == '__main__':
    n = int(input())
    print('%.3f' % solve(n))