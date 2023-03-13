import bisect
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        condition
        1<=k
        1<=arr.len
        """

        def heap_ver():
            from heapq import heappush, heappop

            tree = []
            for a in arr:
                heappush(tree, (abs(a - x), a))

            ans = []
            for i in range(k):
                _, a = heappop(tree)
                heappush(ans, a)

            # ans.sort()

            return [heappop(ans) for _ in range(k)]

        def one_line_ver():
            return sorted(sorted(arr, key=lambda n: (abs(n - x), x))[:k])

        def two_pointer_ver():
            j = bisect.bisect(arr, x)
            i = j - 1

            while j - i - 1 < k:
                if i < 0 and j == len(arr):
                    break

                # reached left boundary
                elif i < 0:
                    j = j + 1

                # reached right boundary
                elif j == len(arr):
                    i = i - 1

                # left side element is closer tha right ones
                elif abs(x - arr[i]) <= abs(arr[j] - x):
                    i = i - 1

                # right side element is closer than left ones
                elif abs(arr[j] - x) <= abs(x - arr[i]):
                    j = j + 1

            return arr[i + 1 : j]

        def two_pointer_ver2():
            l, r = 0, len(arr) - k

            while l < r:
                mid = l + (r - l) // 2
                if x - arr[mid] > arr[mid + k] - x:
                    l = mid + 1
                else:
                    r = mid

            return arr[l : l + k]

        return two_pointer_ver()
        # return heap_ver()


# tow point를 쓸 때
# list에 새로 넣거나
# 아니면 twopointer로 범위 지정을 할 수 있음.

ans = Solution().findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5)
print(ans)


"""
Refer
https://leetcode.com/problems/find-k-closest-elements/discuss/2636835/Python-or-Two-pointers-or-Heap
https://leetcode.com/problems/find-k-closest-elements/discuss/146613/Python-bisect-solution
https://leetcode.com/problems/find-k-closest-elements/discuss/503562/Python-bisect-7-lines
https://leetcode.com/problems/find-k-closest-elements/discuss/1228728/Easy-python-bisect-solution
"""
