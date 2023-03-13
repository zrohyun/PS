def solution(citations):
    answer = 0
    citations.sort(reverse =True)
    h = 0
    for n,c in enumerate(citations):
        if n+1 > c:
            return n
    
    return n+1

# other solution
# 읽기 좋은 코드나 이해하기 좋은 코드는 아닐지도 모르지만
# 간결하다.
# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer