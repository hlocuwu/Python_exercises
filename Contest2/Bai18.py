def solve(n):
    sum = 0
    while n > 0:
        if check_snt(n % 10):
            sum += 1
        n //= 10
    return sum

def check_snt(t):
    if t < 2:
        return False
    for i in range(2, int(t ** 0.5) + 1):
        if t % i == 0:
            return False
    return True
            
if __name__ == "__main__":
    n = int(input())
    print(solve(n))