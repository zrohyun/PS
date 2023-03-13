from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt_s = Counter(s)
        ans = ""
        for c,i in sorted(cnt_s.items(), key=lambda x:(x[1],x[0]), reverse=True):
            ans += c*i

        return ans
