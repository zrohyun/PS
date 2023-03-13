def solution(bridge_length, weight, truck_weights):
    answer = 1
    # truck_weights.sort()
    q = [truck_weights.pop(0)]
    q_cnt = [1]
    
    while q or truck_weights:
        # print(q)
        answer += 1
        # 다리 건너는 트럭 한 칸씩 이동
        q_cnt = [i+1 for i in q_cnt]
        
        # 다리를 지난 트럭 있으면 pop
        if q_cnt[0] > bridge_length:
            q.pop(0)
            q_cnt.pop(0)
             
        # 올라갈 수 있는 트럭이 있으면 올림.
        if truck_weights:
            if truck_weights[0] + sum(q) <= weight and len(q) < bridge_length:
                q.append(truck_weights.pop(0))
                q_cnt.append(1)
        
        
    return answer
