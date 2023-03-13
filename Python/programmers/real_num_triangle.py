def solution(triangle):
    answer = 0
    triangle[1][0] += triangle[0][0]
    triangle[1][1] += triangle[0][0]
    st_li = triangle[1]
    for i in triangle[2:]:
        for n,j in enumerate(i):
            if(n ==0): 
                i[n] = j + st_li[n]
            elif (n == len(i)-1):
                i[n] = j + st_li[n-1]
            else:
                i[n] = max(j+st_li[n-1],j+st_li[n])
        st_li = i
        
        print(triangle)
    
    answer = max(i)
    print(answer)
    return answer

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])