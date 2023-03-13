#https://programmers.co.kr/learn/courses/30/lessons/42626

# skip heap 쓰는 게 그냥 빠를 듯
def solution2(scoville, K):
    answer = 0
    scoville = sorted([i for i in scoville if i<K],reverse=True)
    tmp = []
	
    while scoville:
        
        if len(scoville) ==1 and scoville[0] < K:
                return -1
        elif len(scoville) == 1 and scoville >= K:
            break
        
        while scoville:
            if scoville[0] >= K: 
                tmp.append(scoville[0])
                scoville = scoville[1:]
            else:

                tmp.append(scoville[0] + scoville[1]*2)
                scoville = scoville[2:]
                answer +=1
        
        scoville = tmp
        tmp = []

        # scoville.sort(reverse=True)
    
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq as hq
def solution1(scoville, K):
    answer = 0
    hq.heapify(scoville)
    while scoville[0] < K:

        # if len(heap) == 1 and heap[0] < K:
        #     return -1
        # elif len(heap) == 1 and heap[0] >=K:
        #     return answer
        # else:

        try:
            hq.heappush(scoville,hq.heappop(scoville) + hq.heappop(scoville) *2)
            answer +=1
        except Exception:
            return -1
    

    return answer

print(solution([1,2,3,9,10,12],7))
# print(solution([1],7))
# print(solution([7],7))
