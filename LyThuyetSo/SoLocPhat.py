def solve(n):
    while n > 0:
        digit = n % 10
        if digit not in {0, 6, 8}:
            return False
        n //= 10
    return True
        
if __name__ == '__main__':
    n = int(input())
    if solve(n):
        print(1)
    else:
        print(0)