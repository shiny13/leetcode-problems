import sys 
from typing import List 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        index = -1
        for i in range(len(nums)):
            if target == nums[i]:
                index = i
                break
        print(index)
        return index
        """
        n = len(nums)

        def find(l, r):
            if l > r:
                return -1
            if nums[l] <= nums[r]:
                if nums[l] <= target <= nums[r]:
                    # binary search here
                    while l <= r:
                        m = (l + r) // 2
                        if target == nums[m]:
                            return m
                        elif target > nums[m]:
                            l = m+1
                        else:
                            r = m-1
                return -1
            elif target >= nums[l] or target <= nums[r]:
                # divide and conquer
                m = (l + r) // 2
                return max(find(l, m), find(m+1, r))
            return -1

        return find(0, n-1)

if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    nums = [4,5,6,7,0,1,2] 
    target = 3

    sol = Solution()
    sol.search(nums, target)