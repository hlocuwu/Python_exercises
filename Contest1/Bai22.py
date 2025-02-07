n , S = map(int, input().split())
count = 0
if S % n == 0:
    count = S / n
else:
    count += S // n
    count += 1

print(count)