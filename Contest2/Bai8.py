def solve(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        res.append(i ** 2)
    print(*res) 
    
if __name__ == '__main__':
    n = int(input())
    solve(n)