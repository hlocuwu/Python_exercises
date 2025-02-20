import math
def solve(a, b):
    return math.factorial(min(a, b))
    
if __name__ == "__main__":
    a , b = map(int, input().split())
    print(solve(a, b))