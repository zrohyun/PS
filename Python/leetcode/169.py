class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        #return Counter(nums).most_common(1)[0][0]
        #return max(Counter(nums).keys(), key=counts.get)
        return max(Counter(nums).items(), key= lambda x: x[1])[0]
