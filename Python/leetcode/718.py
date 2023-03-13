from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = [str(i) for i in nums1]
        nums2 = [str(i) for i in nums2]
        a = set()
        l1, l2 = len(nums1), len(nums2)
        if l1 >= l2:
            for n in range(l1):
                for i in range(l1 - n):
                    a.add("".join(nums1[i : i + n + 1]))

            for n in range(l2, 0, -1):
                for i in range(l2 - n):
                    if "".join(nums2[i : i + n]) in a:
                        print(nums2[i : i + n])
                        print(a)
                        return len(nums2[i : i + n])

        else:
            for n in range(l2):
                for i in range(l2 - n):
                    a.add("".join(nums2[i : i + n + 1]))

            for n in range(l1, 0, -1):
                for i in range(l1 - n):
                    if "".join(nums1[i : i + n]) in a:
                        print(nums1[i : i + n])
                        print(a)
                        return len(nums1[i : i + n])

        return 0


print(Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
