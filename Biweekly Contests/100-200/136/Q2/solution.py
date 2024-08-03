#! /usr/bin/env python3

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        row_flips,col_flips=0,0
        rows,cols = len(grid),len(grid[0])
        #checking for row palindromes
        for row in range(rows):
            left,right=0,cols-1
            while(left<right):
                row_flips += grid[row][left]!=grid[row][right]
                left,right = left+1,right-1
        #checking for column palindromes
        for col in range(cols):
            top,bottom=0,rows-1
            while(top<bottom):
                col_flips += grid[top][col]!=grid[bottom][col]
                top,bottom = top+1,bottom-1
        return min(row_flips,col_flips)
        
