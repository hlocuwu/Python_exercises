
n, m = map(int, input().split())

x = (n + 1) // 2  
y = n           
    
res = ((x + m - 1) // m) * m  
    
print(res) if res <= y else print(-1)
