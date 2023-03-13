from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        target_value = image[sr][sc]
        if target_value == newColor: return image
        mxy = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = [(sr,sc)]
        while queue:
            print(queue)
            y,x = queue.pop()
            image[y][x] = newColor
            for nx,ny in mxy:
                if 0<=y+ny<len(image) and 0<=x+nx<len(image[0]):
                    if image[y+ny][x+nx] == target_value:
                        queue.append((y+ny,x+nx))
        return image      

print(Solution().floodFill([[0,0,0],[0,1,1]]
,1
,1
,1))
        