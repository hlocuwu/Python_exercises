def solve(n):
    res = []
    
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n//i)
    res.sort()

    print(len(res))
    print(*res)

if __name__ == '__main__':
    n = int(input())
    solve(n)