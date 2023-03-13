class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict =dict()
        
        for i,v in enumerate(s):
            if v in char_dict:
                char_dict[v] = -1
            else:
                char_dict[v] = i
        
        ans = [i for i in char_dict.values() if i != -1]
        
        return min(ans) if len(ans) else -1


"""
Editor solution
class Solution:
    def firstUniqChar(self, s: str) -> int:
        :type s: str
        :rtype: int

        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1


Other solution
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=Counter(s)
        for i in range(len(s)):
            if c[s[i]]==1:
                return i
        return -1
"""