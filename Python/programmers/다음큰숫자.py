def solution(n):

    answer = 0
    
    ones = bin(n).count("1")
    
    for num in range(n+1, int(1e10)):
        cnt = bin(num).count("1")
        
        if ones == cnt:
            return num
    