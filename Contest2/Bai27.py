def solve(n):
    if n == 0:
        return 0
    return 1 + (n - 1) % 9

if __name__ == '__main__':
    n = int(input())
    print(solve(n))
