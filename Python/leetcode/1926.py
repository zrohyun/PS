from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        is_possible = lambda ny, nx: 0 <= ny < len(maze) and 0 <= nx < len(maze[0])

        y, x = entrance
        q = deque([(0, y, x)])
        visited = set()  # 그냥 maze 방문한 곳에 +로 채워도 될듯
        visited.add((y, x))
        while q:
            cnt, y, x = q.popleft()
            print(cnt, y, x)
            if cnt != 0 and (
                y == 0 or y == len(maze) - 1 or x == 0 or x == len(maze[0]) - 1
            ):
                return cnt
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if (
                    is_possible(ny, nx)
                    and maze[ny][nx] != "+"
                    and (ny, nx) not in visited
                ):
                    q.append((cnt + 1, ny, nx))
                    visited.add((ny, nx))

        return -1
