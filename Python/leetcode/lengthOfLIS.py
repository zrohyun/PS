#https://leetcode.com/problems/longest-increasing-subsequence/
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:

        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

#로그 기록하기
def sol_log_logest(nums):
    dp = [1]*len(nums)
    dp_log = [""]*len(nums)
    for i in range(0,len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                if dp[i] >= (dp[j]+1):
                    dp_log[i] = dp_log[i]
                else:
                    dp[i] = dp[j]+1
                    dp_log[i] = dp_log[j] + str(nums[i])
        print(dp,dp_log)
        if len(dp_log[i]) == 0: 
            dp_log[i] = str(nums[i])
    print(dp_log)
    return max(dp)

print(Solution().lengthOfLIS([0,1,0,3,2,3]))
# sol_log_logest([0,1,0,3,2,3])
from bisect import bisect_left
def lengthOf(nums: list[int]) -> int:
        dp = []
        
        for num in nums:
            # 왜 이진 탐색을 사용하지? 그냥 마지막 요소만 계산하면 되지 않나?
            # 했지만 1 2 9 10 배열이 있을 때 뒤에 5 6 같은 수가 있으면 중간에 삽입해야한다.
            # 근데 중간에 수를 교체하면 연속된게 아니잖아? -> [1, 2, 4, 5, 3, 11,12,7,8]
            # 위의 배열이 어떻게 연산되는지 확인하면 알게된다. 교체를 했을 때 그 뒤에 만족하는 수가 없다면
            # 이전에 만족했던 수열의 길이가 반환될 것이고 만약에 뒤에 더 그 이상을 만족하는 수가 있다면 
            # 다시 그 뒤에 12가 교체되어 새로운 수열이 될 것이다.
            pos = bisect_left(dp, num)
            
            print(dp,pos)    
            if pos == len(dp):
                dp.append(num)
            else:
                dp[pos] = num
        
        return len(dp)

lengthOf([0,1,0,3,2,3])
lengthOf([1, 2, 4, 5, 3, 11,12,7,8])