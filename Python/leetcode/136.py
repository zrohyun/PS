class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        for k,v in Counter(nums).items():
            if v == 1: return k
        # from operator import ixor
        # from functools import reduce
        # return reduce(ixor, nums)
        # return reduce(lambda x,y:x^y,nums)
        
        """
        Crazy bit level solution
        xor -> self xor is return 0 ans there's no need order
        2 ^ 3 ^ 4 ^ 1 ^ 3 ^ 4 ^ 2 = 1, 1 is only numbera
        def singleNumber(self, nums: List[int]) -> int:
	        return reduce(lambda total, el: total ^ el, nums)
        """
        
