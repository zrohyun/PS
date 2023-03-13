#https://programmers.co.kr/learn/courses/30/lessons/12985?language=python3
def solution(n,a,b):
    answer = 0
    
    while a != b:
        answer += 1
        a,b = (a+1)//2, (b+1)//2
        # a = (a+1)//2
        # b = (b+1) //2

    return answer

def solution1(n,a,b):
    return ((a-1)^(b-1)).bit_length()

def solution2(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer
