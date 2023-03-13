# 커리큘럼


def solution():
    n = int(input())
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    times = [0] * n

    for i in range(n):
        time, *pre, dummy = list(map(int, input().split()))
        times[i] = time
        for p in pre:
            graph[p - 1].append(i)
            indegree[i] += 1
    print(indegree)
    print(times)
    print(graph)
    q = []
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    import copy

    running_time = copy.deepcopy(times)
    while q:

        t = q.pop()

        for g in graph[t]:
            indegree[g] -= 1
            running_time[g] += times[i]
            if indegree[g] == 0:
                q.append(g)

    print(running_time)


print(solution())


"""
input sample
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""
