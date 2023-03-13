#가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746
# 정수 [6,10,2]가 주어지면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고
# 6210이 만들 수 있는 가장 큰 수이다.
from itertools import permutations

def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    
    ans = int("".join(numbers))

    return str(ans)


solution([6,10,2])
solution([3, 30, 34, 5, 9])