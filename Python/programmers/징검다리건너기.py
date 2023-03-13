from collections import Counter,deque
def solution(stones, k):
    
    if k == 1:
        return min(stones)
    
    if k == len(stones):
        return max(stones)

    
    def push(win,n):
        while len(win)>0 and win[-1]<n:
            win.pop()
        win.append(n)
    window = deque([])
    res = []
    for i in range(len(stones)):
        # print(window)
        if i+1<k:
            push(window,stones[i])
        else:
            push(window,stones[i])
            res.append(window[0])
            if stones[i+1-k] == window[0]: # 최대값 기간 만료
                
                window.popleft()
    # print(res)
    return min(res)


"""
이분탐색 복잡도 
log(2억) * 200000 => O(log(2^28)*(2^18)) = O(28*2^18)
"""
# def solution(stones, k):
#     left = 1
#     right = 200000000
#     while left <= right:
#         mid = (left + right) // 2
#         cnt = 0
#         for t in stones:
#             if t - mid <= 0:
#                 cnt += 1
#             else:
#                 cnt = 0
#             if cnt >= k:
#                 break
#         if cnt >= k:
#             right = mid - 1
#         else:
#             left = mid + 1
        
#     return left

"""
Counter 혹은 단순한 sliding window 방법
200000 * k 최대길이(20000) => O(200000 * 200000)
"""
# cnt = Counter(stones[:k])
# answer = max(cnt.keys())
# for i in range(k,len(stones)):
#     # print(cnt)
#     cnt[stones[i]] +=1
#     cnt[stones[i-k]] -=1
#     if cnt[stones[i-k]] == 0:
#         del cnt[stones[i-k]]
#     answer = min(answer,max(cnt.keys()))
        