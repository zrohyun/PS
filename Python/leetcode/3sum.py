class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # 0을 만들어야 하는 문제
        # 가장 작은 수부터 시작해야함. 정렬
        nums.sort()
        res = []
        
        # 가장 작은 수부터 시작해 더해나가며 케이스를 탐색해야한다.
        for i in range(len(nums)):
            
            # 같은 숫자는 점프
            if i>0 and nums[i] == nums[i-1]: continue
            
            # 다음 숫자와 가장 큰 숫자부터 
            #가장 작은 숫자와의 조합을 찾아나간다.
            j = i+1 
            k = len(nums)-1
            
            
            while j<k:
                s = nums[i] + nums[j] + nums[k]
                
                if s > 0: k -= 1
                elif s <0: j += 1
                else:
                    res.append([nums[i] ,nums[j] ,nums[k]])
                    j+=1
                    while nums[j-1] == nums[j] and j<k: j+=1 # jump for same element
            
        return res
