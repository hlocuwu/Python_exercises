def solve(n):
    num = 1
    for i in range(n):
        for j in range(n):
            print(num, end = ' ')
            num += 1
        print()
    print()

    for i in range(n):
        for j in range(n):
            print(i + j + 1,  end = ' ')
        print()
    print()

    for i in range(1, n + 1):
        print('~' * (n - i) + f'{i}' * i)
    print()

    for i in range(n):
        num = i + 1
        for j in range(i + 1):
            print(num, end = ' ')
            num += (n - j - 1)
        print()
        
if __name__ == "__main__":
    n = int(input())
    solve(n)