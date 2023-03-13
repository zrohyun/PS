from sys import stdin
input = stdin.readline
def solution():
    N,Kim, Im = list(map(int,input().split()))
    ans = 0
    while True:
        if Kim == Im: return ans

        # if N <=1: return -1
        # if (abs(Kim-Im) == 1) and ((min(Kim,Im)//2)+1 == max(Kim,Im)//2):
            # return ans

        ans += 1
        
        Kim  = Kim//2 + Kim%2 
        Im = Im//2 + Im%2
         
        N = N//2 + N%2

print(solution())