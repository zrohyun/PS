# from collections import defaultdict,Counter
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         ans = defaultdict(list)
#         for s in strs:
#             k = tuple(sorted(Counter(s).items(), key=lambda x: (x[0],x[1])))
#             ans[k].append(s)

#         return ans.values()


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)
        for w in strs:
            key = "".join(sorted(w))
            h[key].append(w)
        return list(h.values())
