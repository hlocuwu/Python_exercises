import math

def solve(n):
    s  = 0
    for i in range(n):
        s += 1 / math.factorial(i)
    return s
    
if __name__ == "__main__":
    n = int(input())
    print('% .4f' % solve(n))