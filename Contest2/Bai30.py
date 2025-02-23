
T = int(input())

numbers = [int(input()) for _ in range(T)]

for N in numbers:
    print("EVEN" if N % 2 == 0 else "ODD")
