import math

def result(N):
    for i in range(2, int(math.sqrt(N))):
        if N % i == 0:
            return 0
    return 1

if __name__ == '__main__':
    N = int(input())
    if result(N):
        print('YES')
    else:
        print('NO')