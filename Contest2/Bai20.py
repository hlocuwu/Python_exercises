def solve(n):
    if n == 1:
        print(-1)
        return
    res = [2] * (n // 2)
    if n % 2 != 0:
        res[-1] = 3

    print(len(res))
    print(*res)    

if __name__ == "__main__":
    n = int(input())
    solve(n)