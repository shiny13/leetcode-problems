import sys 
from typing import List 

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

if __name__ == '__main__':
    input = sys.stdin.read().strip()
    nums = list(map(int, input.split()))

    sol = Solution()
    print(sol.findDuplicate(nums))
