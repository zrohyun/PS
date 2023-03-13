class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # set parameters
        total_len = len(nums1) + len(nums2)
        is_odd = total_len % 2
        mid = int(total_len/2)
        state = -1 # current idx
        
        
        last_val = 0
        while nums1 or nums2:
            state +=1
            v1  = nums1[0] if nums1 else 1e10
            v2  = nums2[0] if nums2 else 1e10
            
            # return condition
            if is_odd and state == mid:
                return min(v1,v2)
            elif not is_odd and state == mid:
                return (last_val + min(v1,v2))/2
                
            if v1 <= v2:
                last_val = v1
                nums1 = nums1[1:]
            elif v2 < v1:
                last_val = v2
                nums2 = nums2[1:]
            
        
    def findMedianSortedArrays_v1(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = 0
        ans = []
        while nums1 or nums2:
            total_len += 1
            v1  = nums1[0] if nums1 else 1e10
            v2  = nums2[0] if nums2 else 1e10
             
            if v1 <= v2:
                ans.append(v1)
                nums1 = nums1[1:]
            elif v2 < v1:
                ans.append(v2)
                nums2 = nums2[1:]
        
        print(ans, total_len)
        if total_len %2:
            return ans[int(total_len/2)]
            
        else:
            idx1,idx2 = int(total_len/2)-1,int(total_len/2)
            return (ans[idx1] + ans[idx2])/2
            
        return 0
            
