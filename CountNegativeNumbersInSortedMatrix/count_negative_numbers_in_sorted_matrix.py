import sys 
from typing import List 

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negatives = 0
        for row in grid:
            length = len(row) - 1
            while length >= 0:
                if row[length] < 0:
                    negatives += 1
                else:
                    break
                length -= 1

        return negatives

if __name__ == '__main__':
    #grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    #grid = [[3,2],[1,0]]
    #grid = [[1,-1],[-1,-1]]
    grid = [[-1]]

    sol = Solution()
    print(sol.countNegatives(grid))
