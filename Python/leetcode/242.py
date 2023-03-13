class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return True if Counter(s) == Counter(t) else False