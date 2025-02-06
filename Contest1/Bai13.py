N = int(input())

y = N // 365
N = N - y * 365
w = N // 7
N = N - w * 7

print(y, w, N)