n = int(input())

cnt100 = n // 100
cnt20 = (n % 100) // 20
cnt10 = ((n % 100) % 20) // 10
cnt5 = (((n % 100) % 20) % 10) // 5
cnt1 = ((((n % 100) % 20) % 10) % 5) // 1

print(cnt100 + cnt20 + cnt10 + cnt5 + cnt1)