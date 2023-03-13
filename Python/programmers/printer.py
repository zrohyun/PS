#https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque
def solution(priorities, location):
    answer = 0
    orderq = deque([(a,i) for i,a in enumerate(priorities)])

    while True:
        if len(orderq) == 1: 
            return answer +1
        # print(orderq)
        tmp = orderq.popleft()
        if tmp[0] >= max(orderq)[0]:
            answer +=1
            if tmp[1] == location:
                return answer
        else: 
            orderq.append(tmp)
        

print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))