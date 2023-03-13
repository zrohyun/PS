# from collections import defaultdict
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         dict_nums = defaultdict(list)
#         for i in range(len(nums)):
#             dict_nums[nums[i]].append(i)
#         print(dict_nums)
#         for key,v in dict_nums.items():
#             # print(key,v)
#             if len(v)<2:
#                 continue

#             if min([v[i] - v[i-1] for i in range(1,len(v))]) <= k:
#                 return True


#         return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = {}
        for i in range(len(nums)):
            if nums[i] not in l:
                l[nums[i]] = i
            else:
                if i - l[nums[i]] <= k:
                    return True
                else:
                    l[nums[i]] = i
        return False
