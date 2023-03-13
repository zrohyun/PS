class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        dp = {}
        for i in range(len(grid[0])):
            r, c = 0, i
            route = []
            while r < len(grid):

                now = grid[r][c]
                left = grid[r][c - 1] if 0 < c <= len(grid[0]) - 1 else 0
                right = grid[r][c + 1] if 0 <= c < len(grid[0]) - 1 else 0
                route.append((r, c))
                if now == 1 and (right == -1 or right == 0):
                    ans.append(-1)
                    break
                if now == -1 and (left == 1 or left == 0):
                    ans.append(-1)
                    break

                if now == 1 and right == 1:
                    r += 1
                    c += 1
                elif now == -1 and left == -1:
                    r += 1
                    c -= 1

            if r == len(grid):
                ans.append(c)
                for r in route:
                    dp[r] = c

        return ans


# 더 간단한 풀이
# class Solution:
#     def findBall(self, grid: List[List[int]]) -> List[int]:
#         lst = []
#         for i in range(len(grid[0])):
#             loc = i

#             for j in range(len(grid)):
#                 if grid[j][loc] == 1:
#                     if loc == len(grid[0]) - 1 or grid[j][loc + 1] == -1:
#                         loc = -1
#                         break
#                     loc += 1
#                 else:
#                     if loc == 0 or grid[j][loc - 1] == 1:
#                         loc = -1
#                         break
#                     loc -= 1

#             lst.append(loc)

#         return lst
