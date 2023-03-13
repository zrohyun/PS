from collections import deque
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        set에서 dfs로 찾기 maxlen까지 찾고 없으면 넘기기
        """
        maxdepth = max([len(s) for s in words])
        words = set(words)

        # print(maxdepth, words)

        loc = [0, 0]
        word = board[loc[0]][loc[1]]
        visited = set([(0, 0)])
        m, n = len(board), len(board[0])
        q = deque()
        for i in range(m * n):
            r, c = i // n, i % n
            q.append([[r, c], board[r][c], set([(r, c)])])

        ans = set()
        while q:
            # print(q)
            l, w, v = q.popleft()

            if len(w) > maxdepth:
                break

            if w in words:
                ans.add(w)

            for nr, nc in self.next(l, m, n, v):
                q.append(([nr, nc], w + board[nr][nc], v.union(set([(nr, nc)]))))

        return list(ans)

    def next(self, loc, m, n, visited):

        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = []
        for mv in move:
            nr = loc[0] + mv[0]
            nc = loc[1] + mv[1]
            if (nr, nc) not in visited and 0 <= nr < m and 0 <= nc < n:
                ans.append((nr, nc))

        return ans


assert (
    Solution().findWords(
        board=[["a", "a"]],
        words=["aaa"],
    )
    == []
)
