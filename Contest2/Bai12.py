def solve(n):
    s = 0
    for i in range(1, n + 1):
        s += i * 2
    return s

if __name__ == "__main__":
    n = int(input())
    print(solve(n))