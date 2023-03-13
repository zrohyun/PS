from typing import List
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(L, -H, R) for (L, R, H) in buildings]
        events += [(R, 0, 0) for (_, R, _) in buildings]
        events.sort()

        ans = [[0, 0]]
        live = [[0, float("inf")]]

        for (L, negH, R) in events:  # 현 시점(current)
            while live[0][1] <= L:  # 현 시점보다 이전에 건물들 pop
                heapq.heappop(live)

            if negH:  # 새로운 건물
                heapq.heappush(live, (negH, R))

            # 새로운 건물이 들어왔는데
            # 이전 건물보다 높다? add
            if ans[-1][0] != -live[0][0]:
                ans.append((L, -live[0][0]))

        return ans[1:]


class Solution1:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        from heapq import heappush, heappop

        sky = []
        op = []

        # save height each point
        # left point better than right point when they are same
        for i, j, k in buildings:
            sky.append([i, -k])
            sky.append([j, k])
        sky.sort()

        q = [0]
        prev_max = 0

        for p, h in sky:

            # if h<0, left point
            # else right point, highest point remove
            if h < 0:
                q.append(-h)
            else:
                q.remove(h)

            cur_max = max(q)
            if prev_max != cur_max:
                op.append([p, cur_max])
                prev_max = cur_max

        return op


Solution().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
