def solve(n):
    if n == 0:
        return 1
    cnt = 0
    while n > 0:
        cnt += 1
        n //= 10
    return cnt

if __name__ == "__main__":
    n = int(input())
    print(solve(n))