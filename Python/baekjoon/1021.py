from collections import deque

def solution():
    N,M = list(map(int,input().split()))
    nums = list(map(int, input().split()))
    deq = deque(range(1,N+1))
    ans = 0
    for i in nums:
        cnt = 0
        rcnt = lcnt = 0
        for _ in range(len(deq)):
            cnt +=1
            tmp = deq.pop()
            if tmp == i: rcnt = cnt
            deq.appendleft(tmp)

        cnt = 0
        for _ in range(len(deq)):
            tmp = deq.popleft()
            if tmp == i: lcnt = cnt
            deq.append(tmp) 
            cnt +=1

        if rcnt >= lcnt:
            deq.rotate(-lcnt)
            deq.popleft()
        else:
            deq.rotate(rcnt)
            deq.popleft()


        ans += min(rcnt,lcnt)
    
    return ans


print(solution())