def solve(c1, c2, c3, c4, c5):
    if (c1 + c2 + c3 + c4 + c5) % 5 != 0:
        return -1
    coin = (c1 + c2 + c3 + c4 + c5) / 5
    if coin != 0:
        return coin
    return -1
if __name__ == '__main__':
    c1, c2, c3, c4, c5 = map(int, input().split())
    print(solve(c1, c2, c3, c4, c5))