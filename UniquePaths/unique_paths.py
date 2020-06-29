import sys 
from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        return factorial(m+n-2)//factorial(m-1)//factorial(n-1)

if __name__ == '__main__':
    input = sys.stdin.read().strip()
    data = list(map(int, input.split()))

    sol = Solution()
    print(sol.uniquePaths(data[0], data[1]))
