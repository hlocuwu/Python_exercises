def solve(n):
    price = 28 #168
    bia = n // price # 6
    vo = bia # 6

    while vo >= 3:
        new = vo // 3 # 2
        bia += new # 8
        vo -= new * 3

    return bia
        

if __name__ == "__main__":
    n = int(input())
    print(solve(n))