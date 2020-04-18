import sys
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) <= 0 or grid is None:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if r==0 and c==0:
                    continue
                if r-1<0:
                    grid[r][c] = grid[r][c] + grid[r][c-1]
                elif c-1<0:
                    grid[r][c] = grid[r][c] + grid[r-1][c]
                else:
                    grid[r][c] = min(grid[r][c] + grid[r][c-1], grid[r][c] + grid[r-1][c])
        print(grid[rows-1][cols-1])
        return grid[rows-1][cols-1]

if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = list(input.split())
    
    #sample input
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    sol = Solution()
    sol.minPathSum(grid)