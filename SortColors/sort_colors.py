import sys
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                temp = nums[mid]
                nums[mid] = nums[low]
                nums[low] = temp 
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                temp = nums[mid]
                nums[mid] = nums[high]
                nums[high] = temp 
                high -= 1
        print(nums)


if __name__ == '__main__':
    input = sys.stdin.read()
    nums = list(map(int, input.split()))

    sol = Solution()
    sol.sortColors(nums)
