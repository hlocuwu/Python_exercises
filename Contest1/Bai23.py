import math
n, m = map(int, input().split())

x = (n + 1) // 2  # Số bước tối thiểu (ceil(n / 2))
y = n             # Số bước tối đa
    
res = ((x + m - 1) // m) * m  # Tìm số nhỏ nhất >= x chia hết cho m
    
print(res) if res <= y else print(-1)
