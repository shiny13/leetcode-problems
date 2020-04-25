import sys
from typing import List 

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1
        i = len(nums) - 1
        while i >= 0:
            if i + nums[i] >= lastPos:
                lastPos = i
            i-=1
        return lastPos == 0

if __name__ == '__main__':
    input = sys.stdin.read()
    nums = list(map(int, input.split()))

    sol = Solution()
    print(sol.canJump(nums))
