import math

def solve(n):
    sum = 0
    for i in range(1, n + 1):
        sum += math.factorial(i)
    return sum

if __name__ == '__main__':
    n = int(input())
    print(solve(n))