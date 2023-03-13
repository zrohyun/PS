class Solution:
    """
    floyd-warshall version
    short path from every node
    """

    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        # make graph board
        from decimal import Decimal

        element = set()

        for i, j in equations:
            element.add(i)
            element.add(j)

        # graph dict
        gd = {n: i for i, n in enumerate(element)}
        INF = int(1e10)
        n = len(element)

        # graph init
        graph = [[INF] * n for _ in range(n)]

        # self division(self connection)
        for i in range(n):
            graph[i][i] = 1

        for (i, j), v in zip(equations, values):
            graph[gd[i]][gd[j]] = v
            graph[gd[j]][gd[i]] = Decimal(1 / v)

        for m in element:
            for s in element:
                for d in element:
                    if graph[gd[s]][gd[m]] != INF and graph[gd[m]][gd[d]] != INF:
                        graph[gd[s]][gd[d]] = float(graph[gd[s]][gd[m]]) * float(
                            graph[gd[m]][gd[d]]
                        )

        ans = []
        for qs, qd in queries:
            try:
                if graph[gd[qs]][gd[qd]] != INF:
                    ans.append(float(graph[gd[qs]][gd[qd]]))
                else:
                    raise KeyError

            except KeyError as ke:
                ans.append(-1)
            except Exeption as e:
                pass

        return ans
