import sys 
from typing import List 

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        beg, end = 0, len(nums)
        while beg < end:
            mid = (beg + end)//2
            if nums[mid] >= target:
                end = mid
            else:
                beg = mid + 1
        return beg

if __name__ == '__main__':
    #nums, target = [1,3,5,6], 5
    #nums, target = [1,3,5,6], 2
    nums, target = [1,3,5,6], 7
    #nums, target = [1,3,5,6], 0

    sol = Solution()
    print(sol.searchInsert(nums, target))
