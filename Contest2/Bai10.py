def solve():
    N = int(input()) 
    numbers = list(map(int, input().split()))

    for num in numbers:
        if num == 2022:
            print("YES")
            return  

    print("NO")

if __name__ == "__main__":
    solve()
