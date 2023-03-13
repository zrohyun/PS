from collections import defaultdict


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        a = defaultdict(lambda: [0, 0])

        for w, l in matches:
            a[w][0] += 1
            a[l][1] += 1
        ans = [[] for i in range(2)]
        for k, v in a.items():
            if v[1] == 0:
                ans[0].append(k)

            if v[1] == 1:
                ans[1].append(k)

        return [sorted(i) for i in ans]
