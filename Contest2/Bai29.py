def solve(arr):
    sum = 0
    for i in arr:
        if i % 2 == 0:
            sum += i
    return sum

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))