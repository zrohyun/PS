from copy import deepcopy as dpcp
def solution(triangle):
    answer = 0
    st_li = triangle[0]
    for i in triangle[1:]:
        for n,j in enumerate(i):
            if(n ==0): 
                i[n] = j + st_li[n]
            elif (n == len(i)-1):
                i[n] = j + st_li[n-1]
            else:
                i[n] = max(j+st_li[n-1],j+st_li[n])
        st_li = dpcp(i)
        
    
    answer = max(st_li)
    return answer


N = int(input())
tri = [list(map(int,input().split())) for _ in range(N)]
print(solution(tri))