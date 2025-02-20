def solve(n):
    price = 28 
    bia = n // price 
    vo = bia 

    while vo >= 3:
        new = vo // 3 
        bia += new 
        vo  = vo % 3 + new

    return bia
        

if __name__ == "__main__":
    n = int(input())
    print(solve(n))