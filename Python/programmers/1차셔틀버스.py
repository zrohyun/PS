from collections import deque
def solution(n, t, m, timetable):
    "9시부터 n회 t분 간격 도착, m명의 승객 탑승 가능"
    crews = deque(sorted([int(i[:2])*60 + int(i[3:]) for i in timetable]))
    start = 540
    cnt, last_crew = 0, 0
    for i in range(n):
        cnt, last_crew = 0,0
        
        while cnt < m and crews:
            if crews[0] <= start:
                cnt += 1
                last_crew = crews.popleft()
            else:
                break
        
        if i == n-1:
            break
        start += t 
        
    time = last_crew - 1 if cnt == m else start
    
    
    return f"{time//60:02d}:{time%60:02d}"
        
        