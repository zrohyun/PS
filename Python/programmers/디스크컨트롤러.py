import heapq


def solution(jobs):
    answer = 0
    time = 0
    length = len(jobs)
    jobs.sort()
    heap = []
    while len(jobs) != 0 or len(heap) != 0:

        # 현 시점 요청이 시작된 작업들 큐에 넣기 (minheap)
        while len(jobs) != 0 and jobs[0][0] <= time:
            heapq.heappush(heap, jobs.pop(0)[::-1])

        if len(heap) == 0:
            time = jobs[0][0]
            continue

        process = heapq.heappop(heap)
        time += process[0]
        answer += time - process[1]

    return answer // length