from math import *

def pt_NT(N):
    if N<2: return False 
    i = 2 
    count = 0 
    while i <= isqrt(N)+1:
        mu = 0 
        while N%i ==0:
            mu+=1 
            N//=i 
            if mu>1:
                return False 
            elif mu == 1: 
                count+=1 
        if count>3:
            return False
        i+=1 
    if N>1: 
        count +=1 
    return count==3

if __name__ == '__main__':
    N = int(input())
    if pt_NT(N) : print('1')
    else : print('0')