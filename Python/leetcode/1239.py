# class Solution:
#     def maxLength(self, arr: List[str]) -> int:
#         arr = sorted(arr, key=lambda x: len(x))
#         ans = len(arr[0])

#         for i in range(len(arr)):
#             i_set = set(arr[i])
#             for j in range(i+1,len(arr)):
#                 if i_set.intersection(set(arr[j])):
#                     ans = max(ans, len(arr[i]) + len(arr[j]))
#                     break
#         return ans


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        res = [""]
        output = 0
        for word in arr:
            for r in res:
                new_r = r + word
                if len(new_r) != len(set(new_r)):
                    continue
                res.append(new_r)
                output = max(output, len(new_r))

        return output
