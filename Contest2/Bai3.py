def solve(n):
    sum = 0
    for i in range(3, n + 1, 3):
        sum += i
    return sum

if __name__ == '__main__':
    n = int(input())
    print(solve(n))