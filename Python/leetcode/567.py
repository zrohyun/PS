
#https://leetcode.com/problems/permutation-in-string/
#Permutations in String

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # from itertools import permutations as per
        # pocket = {"".join(i) for i in per(s1,len(s1))}
        
        #sol2 - failure
        # for i in range(len(s2)-len(s1)+1):
        #     if s2[i:i+len(s1)] in pocket:
        #         return True
        
        #sol2 - failure
        # for i in per(s1,len(s1)):
        #     if s2.find("".join(i)) != -1:
        #         return True
        
        #sol3
        # originCounter = Counter(s1)
        # lastseen
        # pocket = set(s1)
        # lens1 = len(s1)
        # cnt = 0
        # for i in list(s2):
        #     if i in :
        #         cnt += 1
        #     else:
        #         cnt = 0
        
        # return False if cnt != lens1 else True
        
        #sol4
        from collections import Counter
        cnt,len_s1 = Counter(s1),len(s1)
        
        for i,v1 in enumerate(s2):
            
            if v1 in cnt:
                cnt[v1] -= 1
            if i >= len_s1 and (v2:=s2[i-len_s1]) in cnt:
                cnt[v2] +=1
            
            if not any(cnt.values()):
                return True
            

        return False