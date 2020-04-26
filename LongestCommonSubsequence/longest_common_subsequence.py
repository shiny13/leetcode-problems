import sys

# Top down solution using DP
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        dp = [[-1 for x in range(len(text2))] for x in range(len(text1))] 
        #print(dp)

        return self.lcs(text1, text2, 0, 0, dp)
    
    def lcs(self, text1, text2, i, j, dp):
        #print("lcs i {} j {}".format(i,j))
        if i == len(text1) or j == len(text2):
            return 0
        #print(dp[i][j])
        if dp[i][j] != -1:
            return dp[i][j]
        if text1[i] == text2[j]:
            dp[i][j] = self.lcs(text1, text2, i+1, j+1, dp) + 1
            return dp[i][j]
        else:
            dp[i][j] = max(self.lcs(text1, text2, i+1, j, dp), self.lcs(text1, text2, i, j+1, dp))
            return dp[i][j]
        



if __name__ == '__main__':
    input = sys.stdin.read()
    #nums = list(map(int, input.split()))
    data = input.split()

    sol = Solution()
    print(sol.longestCommonSubsequence(data[0], data[1]))
