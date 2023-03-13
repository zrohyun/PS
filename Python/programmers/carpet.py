def solution(brown, yellow):
    answer = []
    size = brown + yellow
    for i in range(1,size+1):
        if size % i == 0:
            # a,b = i, size//i
            if ((a:=i) + (b:=size//i) -2)*2 == brown:
                return sorted([a,b], reverse=True)
            
    return answer