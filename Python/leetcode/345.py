from collections import deque
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a','e','i','o','u',"A",'E','I','O','U'])
        s = list(s)
        l , r = 0, len(s)-1
        while l < r:
            while l<r and s[l] not in vowels:
                l+=1
            while l<r and s[r] not in vowels:
                r-=1
            
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r],s[l]
                l+=1
                r-=1
        return "".join(s)

    def reverseVowels_v2(self, s: str) -> str:
        vowels = set(['a','e','i','o','u',"A",'E','I','O','U'])
        s = list(s)
        l , r = 0, len(s)-1
        while l < r:
            if s[l] not in vowels:
                l +=1
                continue
            
            if s[r] not in vowels:
                r -=1
                continue
            
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r],s[l]
                l+=1
                r-=1
        # print(s)
        return "".join(s)


    def reverseVowels_v1(self, s: str) -> str:
        vowels = set(['a','e','i','o','u',"A",'E','I','O','U'])
        s = list(s)
        v_order = deque([])
        for i in range(len(s)):
            if s[i] in vowels:
                v_order.append(s[i])
                s[i] = 0
        for i in range(len(s)):
            if s[i] == 0:
                s[i] = v_order.pop()

        return "".join(s)
            