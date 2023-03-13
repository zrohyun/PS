class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # sum(nums) - sum(set(nums)) gets duplicate number

        # (len(nums) * (len(nums) + 1))//2 gets sum of correct numbers from 1 to n
        # Alternatively you could do sum([i for i in range(1, len(nums) + 1])

        # Therefore (len(nums) * (len(nums) + 1))//2 - sum(set(nums)) gets the lost number
        return [
            sum(nums) - sum(set(nums)),
            (len(nums) * (len(nums) + 1)) // 2 - sum(set(nums)),
        ]
