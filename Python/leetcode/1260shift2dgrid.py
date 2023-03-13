from typing import List
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        from itertools import chain
        k = k % (len(grid)*len(grid[0]))
        cols = len(grid[0])
        grid = list(chain(*grid))
        grid[:] = grid[-k:] + grid[:-k]
        
        return [grid[i:i + cols] for i in range(0, len(grid), cols)]