import sys 
from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        dp[m-1][n], dp[m][n-1] = 1, 1
        for i in range(m-1): dp[i][n] = float("inf")
        for j in range(n-1): dp[m][j] = float("inf")
            
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
                for _i in range(m+1): print(dp[_i])
                print(' ')
        
        return dp[0][0]

if __name__ == '__main__':

    dungeon = [
        [-2,-3,3],
        [-5,-10,1],
        [10,30,-5]
    ]

    sol = Solution()
    print(sol.calculateMinimumHP(dungeon))
