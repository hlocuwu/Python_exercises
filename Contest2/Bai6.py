def solve(n):
    sum = 0
    sqrtN = int(n ** 0.5)
    for i in range(1, sqrtN + 1):
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
    return sum

if __name__ == '__main__':
    n = int(input())
    print(solve(n))