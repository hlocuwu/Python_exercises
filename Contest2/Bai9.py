def solve(n):
    res = 1
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res *= i
            if i != n // i:
                res *= (n // i)
    
    return res

if __name__ == '__main__':
    n = int(input())
    print(solve(n))