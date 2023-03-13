from heapq import heappop, heappush, heapify


def solution(n, info):
    ans = []
    heapify(ans)
    score = 10
    appeach = 0
    lion = 0
    lion_scores = []

    # 10점부터 2선해서 dfs
    # 10점일 때 appeach,lion score append(backtracking)

    q = []
    if info[0]:
        q.append([appeach + 10, lion, lion_scores + [0], score - 1, n])
    use = info[10 - score] + 1
    if n >= use:
        q.append([appeach, lion + 10, lion_scores + [use], score - 1, n - use])

    while q:
        a, l, ls, s, cnt = q.pop()
        if s == 0:
            ls = ls + [cnt]
            if a < l:
                heappush(ans, (a - l, ls))
            # print((a - l, ls))
            continue

        if info[10 - s]:
            q.append([a + s, l, ls + [0], s - 1, cnt])
        else:
            q.append([a, l, ls + [0], s - 1, cnt])
        use = info[10 - s] + 1
        if cnt >= use:
            q.append([a, l + s, ls + [use], s - 1, cnt - use])
    for a in ans:
        print(a)
    temp = []
    if ans:
        l_gap, hist = heappop(ans)
        temp.append(hist[::-1])
        while ans:
            t1, t2 = heappop(ans)
            if l_gap != t1:
                break

            temp.append(t2[::-1])

        temp.sort(reverse=True)
    print(temp)
    #     def dfs(appeach:int, lion:int, lion_scores:list,score:int,n:int,)-> None:
    #         if n==0 and appeach >= lion:
    #             return

    #         #appeach win
    #         dfs(appeach + score,lion, lion_scores + [0], score-1,n)

    #         #lion win
    #         use = info[10-score] +1
    #         dfs(appeach,lion + score,lion_scores + [use],score-1,n-use)

    #     #appeach win
    #     dfs(appeach + 10,lion, lion_scores + [0], 10-1,n)

    #     #lion win
    #     use = info[10-score] +1
    #     dfs(appeach,lion + 10,lion_scores+ [use],10-1,n-use)

    return temp[0][::-1] if temp else [-1]


# solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3])
# solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1])
solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
# solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
