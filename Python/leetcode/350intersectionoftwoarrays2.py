class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # onedex = twodex = 0
        # nums1.sort()
        # nums2.sort()
        # ans = []
        # while onedex < len(nums1) and twodex < len(nums2):
        #     if nums1[onedex] == nums2[twodex]:
        #         ans.append(nums1[onedex])
        #         onedex += 1
        #         twodex += 1
        #     elif nums1[onedex] < nums2[twodex]:
        #         onedex +=1
        #     else:
        #         twodex +=1
                
        #counter solution
        from collections import Counter
        setnum = set(nums1) & set(nums2)
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        # print(cnt1,cnt2,setnum)
        ans = []
        for i in setnum:
            for j in range(min(cnt1[i],cnt2[i])):
                ans.append(i)    
        # print(ans)
        
        return ans
    
        






"""Other Solution
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        for i in nums1:
            if i in dict1:
                dict1[i] +=1
            else:
                dict1[i] = 1
        res = []
        for i in nums2:
            if i in dict1 and dict1[i]>0:
                res.append(i)
                dict1[i] -=1
        return res
"""
