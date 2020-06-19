import sys 
from typing import List 

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations is None or len(citations) == 0: 
            return 0
        n, res = len(citations), 0
        mid, start, end = 0, 0, len(citations) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if (citations[mid] == n - mid):
                return n - mid
            elif citations[mid] < n - mid:
                start = mid + 1
            else:
                res = n - mid 
                end = mid - 1 

        return res

if __name__ == '__main__':
    input = sys.stdin.read()
    citations = list(map(int, input.split()))
    
    sol = Solution()
    print(sol.hIndex(citations))
