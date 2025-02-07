def solve(h, m):
    hpd = 24 * 60
    tmp = h * 60 + m
    return hpd - tmp
    

if __name__ == '__main__':
    h, m = map(int, input().split())
    print(solve(h, m))