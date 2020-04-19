import sys 
from typing import List 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        for i in range(len(nums)):
            if target == nums[i]:
                index = i
                break
        print(index)
        return index

if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    nums = [4,5,6,7,0,1,2] 
    target = 3

    sol = Solution()
    sol.search(nums, target)