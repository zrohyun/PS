# deque maxlen을 이용해서 하는 방법도 있을 것 같음.
def solution(n):
    ans = 0
    for i in range(1, n + 1):
        sum_ = 0
        for j in range(i, n + 1):
            sum_ += j
            if sum_ == n:
                ans += 1
                break
            elif sum_ > n:
                break

    return ans


## 등차수열 이용
# def solution(num):
#     return len([i  for i in range(1,num+1,2) if num % i is 0])
