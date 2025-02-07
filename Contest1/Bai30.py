def solve(n):
    if n < 2:
        return 0
    return (n * (n - 1)) // 2

if __name__ == '__main__':
    n = int(input())
    print(solve(n))