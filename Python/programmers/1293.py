import copy
from typing import List
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]
        # (r,c,k,walk)
        q = deque([(0, 0, 0, 0)])
        visited = set()

        while q:
            r, c, kk, walk = q.popleft()

            if (r, c, kk) in visited or kk > k:
                continue

            if (r, c) == (m - 1, n - 1):
                return walk

            visited.add((r, c, kk))

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < m and 0 <= nc < n:
                    q.append((nr, nc, kk + grid[r][c], walk + 1))
        return -1


Solution().shortestPath([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1)

Solution().shortestPath([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1)
