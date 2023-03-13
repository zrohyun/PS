from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        log = dict()
        for i ,v in enumerate(numbers):
            if v in log:
                return [log[v]+1,i+1]
            else:
                log[target - numbers[i]] = i