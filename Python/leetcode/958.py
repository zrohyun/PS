class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        even_val = 0
        
        for i in nums:
            if self.is_even(i):
                even_val += i
        
        for q in queries:
            v,idx = q
            
            if self.is_even(nums[idx]):
                even_val -= nums[idx]
            
            nums[idx] += v
            
            
            if self.is_even(nums[idx]):
                even_val += nums[idx]
            
            
            ans.append(even_val)
        
        print(ans)
        
        return ans
        
                
    
    def is_even(self,i:int):
        if abs(i)%2 == 1:
            return False
        
        return True
        
        
