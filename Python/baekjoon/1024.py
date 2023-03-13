from sys import stdin
input = stdin.readline

def solution():
    N,L = list(map(int,input().split()))
    ans = False
    for i in range(L,101):
        a = [0]*10
        # if N // i - i//2 >= 0:
        #     a = list(range(N // i - i//2,N // i - i//2 + i))
        # if N // i - i//2 +1>=0:
        #     b = list(range(N // i - i//2 +1,N // i - i//2 + i+1))
        if N//i - i//2 >=-1:
            a = list(range(N // i - i//2,N // i - i//2 + i+1))
        else: break
        
        if a[1] < 0: break
        
        if sum(a[:-1]) == N: 
            return a[:-1]
        elif sum(a[1:]) == N:
            return a[1:]

    return [-1]



print(" ".join(map(str,solution())))