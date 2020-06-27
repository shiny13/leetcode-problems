import sys 
import math 

class Solution:
    def numSquares(self, n: int) -> int:
        if n<=0:
            return 0
        dp = [i for i in range(n+1)]
        for j in range(1,n+1):
            for k in range(1,int(math.sqrt(j))+1):
                dp[j] = min(dp[j],dp[j-k*k]+1)
        return dp[n]

if __name__ == '__main__':
    input = sys.stdin.read().strip()
    n = int(input)

    sol = Solution()
    print(sol.numSquares(n)) 
