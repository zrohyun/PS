class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [pref[0]]
        for i in range(len(pref) - 1):
            res.append(pref[i] ^ pref[i + 1])

        return res