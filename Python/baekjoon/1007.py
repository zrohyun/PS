from functools import reduce
import math
from itertools import combinations as comb
from sys import stdin
input = stdin.readline
def solution():
    n = int(input())    
    p = [tuple(map(int,input().split())) for _ in range(n)]
    # all_vector = tuple(reduce(lambda a,b: (a[0]+b[0],a[1]+b[1]), p))
    avx,avy = 0,0
    for x,y in p:
        avx,avy = avx+x,avy+y

    # ans = float("inf")
    ans = math.maxsize()
    # check = {}
    combli = list(comb(range(n),n//2))
    for i in combli[:len(combli)//2]:
        
        # if i in check: continue
        
        # print(p[list(i)])
        # st = reduce(lambda a,b: (a[0]+b[0],a[1]+b[1]), [p[k] for k in i])

        # st = reduce(lambda a,b: (a[0]+b[0],a[1]+b[1]), list(map(lambda k : p[k], i)))
        stx,sty = 0,0
        for k in i:
            stx,sty = stx+p[k][0], sty +p[k][1]
        l =  (avx - stx,avy-sty)
        
        #hashing
        # c = tuple(j for j in range(n) if j not in i)

        # check[c] = 1
        
        ans = min(ans, len_of_vector(stx,sty,*l))

        # if l not in check:
        #     check[l] = 1
        #     ans = min(ans, len_of_vector(*st,*l))
            
    return ans
    


def len_of_vector(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


t = int(input())
for i in range(t):
    print(solution())

#dfs
#https://suriisurii.tistory.com/61