class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        # for i in range(len(prices)):
        #     for j in range(i,len(prices)):
        #         ans = max(ans, prices[j]-prices[i])
        
        cur = prices[0]
        for i in prices[1:]:
            cur = min(i,cur)
            ans = max(ans,i-cur)
            # if i < cur:
            #     cur = i
            # else:
            #     ans = max(ans,i-cur)
        
        return ans