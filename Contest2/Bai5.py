def solve(n):
    s = 0
    for i in range(1, n + 1):
        s += 1 / (2 * i)
    return s

if __name__ == '__main__':
    n = int(input())
    print('%.5f' % solve(n))