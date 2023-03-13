class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        ran_cnt = Counter(ransomNote)

        
        for i in magazine:
            if i in ran_cnt:
                if ran_cnt[i] != 0:
                    ran_cnt[i] -= 1 
            
            if sum(ran_cnt.values()) ==0:
                return True
            
        return False


"""
Other Solution
class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        :type ransomNote: str
        :type magazine: str
        :rtype: bool

        from collections import Counter

        if len(ransomNote) > len(magazine): return False
        if not ransomNote: return True
        if not magazine: return False

        countDiff = Counter(magazine)
        countDiff.subtract(Counter(ransomNote))
        return min(countDiff.values()) > -1

    for i in "abcdefghijklmnopqrstuwxyz":
        if magazine.count(i) < ransomNote.count(i):
            return False

    return True
"""