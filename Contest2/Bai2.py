def solve(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 2
    return sum

if __name__ == '__main__':
    n = int(input())
    print(solve(n))