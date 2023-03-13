from collections import defaultdict
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """
        https://leetcode.com/problems/satisfiability-of-equality-equations/discuss/2626555/Python-oror-DFS-oror-graph
        https://leetcode.com/problems/satisfiability-of-equality-equations/discuss/2626060/Python-Graph-Solution

        """
        graph = defaultdict(set)
        not_equal = []

        for i in equations:
            # equal letters dict
            if i[1:3] == "==":
                graph[i[0]].add(i[-1])
                graph[i[-1]].add(i[0])
            else:
                # not equal pair list
                not_equal.append((i[0], i[-1]))

                # retrieve not equal pair in equal dict
        for i in not_equal:
            if self.dfs(i[0], i[-1], graph, set()):  # is it equal or not
                return False
        return True

    def dfs(self, beg, target, graph, visited):
        if beg == target:
            return True

        visited.add(beg)
        # compare equal letters with beg and target that not equal with beg
        for i in graph[beg]:
            if i not in visited and self.dfs(i, target, graph, visited):
                return True

        return False


class Solution:
    """
    Unionfind Solution
    https://leetcode.com/problems/satisfiability-of-equality-equations/discuss/2625908/O(n)-Easy-solution
    """

    def equationsPossible(self, equations: List[str]) -> bool:
        unionFind = {}

        def find(x):
            unionFind.setdefault(x, x)
            if x != unionFind[x]:
                unionFind[x] = find(unionFind[x])
            return unionFind[x]

        def union(x, y):
            unionFind[find(x)] = find(y)

        # 첫 단어를 시작으로 dict를 만듦. 결국 모든 equation을 돌면
        # 같은 union 끼리는 dict를 타고가다보면 연결됨. 이를 이용하면 됨.
        for e in equations:
            if e[1] == "=":
                union(e[0], e[-1])

        for e in equations:
            if e[1] == "!":
                if find(e[0]) == find(e[-1]):
                    return False
        return True


# 결국은 동일한 성질을 가진 집단끼리 묶는 것.
# set으로 묶느냐 혹은 dict로 union이 연결되게 하느냐.
