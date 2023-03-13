from collections import defaultdict, deque


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        """
        condition
        n == quiet.length
        1<=n
        i보다 가난한데 시끄럽다면 대체
        """
        n = len(quiet)
        # return self.dfs_sol(richer,quiet, n)
        return self.topological_sort(richer, quiet, n)

    def dfs_sol(self, richer, quiet, n):
        def dfs(adj_list, ans, node, par):
            ans[node] = par

            for neig in adj_list[node]:
                if ans[neig] == -1:
                    dfs(adj_list, ans, neig, par)

        order = [(quietness, idx) for idx, quietness in enumerate(quiet)]
        order.sort()
        n = len(quiet)

        # form adj list
        adj_list = defaultdict(list)
        for par, child in richer:
            adj_list[par].append(child)

        ans = [-1] * n
        while order:
            _, node = order.pop(0)

            # update all possible child for the node using dfs
            # if not updated yet
            # no need of visited since there would be no cycles
            if ans[node] == -1:
                dfs(adj_list, ans, node, node)

        return ans

    def topological_sort(self, richer, quiet, n):

        graph = [[] for i in range(n)]
        indegree = [0] * (n)

        ans = [i for i in range(n)]

        for i, j in richer:
            # i is richer than j
            graph[i].append(j)
            indegree[j] += 1

        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            rich = q.popleft()
            for poor in graph[rich]:
                # rich보다 poor이 시끄러우면 바꿈
                if quiet[ans[poor]] > quiet[ans[rich]]:
                    ans[poor] = ans[rich]
                indegree[poor] -= 1
                if indegree[poor] == 0:
                    q.append(poor)

        return ans


"""
reference
https://leetcode.com/problems/loud-and-rich/discuss/1395206/Python-oror-DFS-oror-Directed-Graph-oror-Beats-95
https://leetcode.com/problems/loud-and-rich/discuss/1383787/Python-topological-sort-robbing-everyone-from-rich-to-poor
https://leetcode.com/problems/loud-and-rich/discuss/1473739/Well-documented-python-solution
https://leetcode.com/problems/loud-and-rich/discuss/1678133/Python-Topological-Sort-Solution
https://leetcode.com/problems/loud-and-rich/discuss/2241019/Python-Topological-Sort-Solution
"""
