#https://leetcode.com/problems/spiral-matrix-ii/
#Spiral Matrix 2

from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        RIGHT = (0, 1);LEFT = (0, -1);
        DOWN = (1, 0);UP = (-1, 0)
        
        route = [RIGHT,DOWN,LEFT,UP]
        mat = [[0]*n for _ in range(n)]
        
        x,y,ridx = -1,0,0
        ny,nx = route[ridx]
        
        condition = lambda x,y: 0<=x<n and 0<=y<n and not mat[y][x]
        
        for i in range(1,n**2+1):
            if not condition(x+nx,y+ny):
                ridx = (ridx+1)%4
                ny,nx = route[ridx]
            y += ny;x+=nx
            mat[y][x] = i
        
        return mat