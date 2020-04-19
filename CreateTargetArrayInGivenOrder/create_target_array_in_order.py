import sys
from typing import List 

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            idx = index[i]
            if idx+1 > len(target):
                target.append(nums[i])
            else:
                target.insert(idx, nums[i]) 

        print(target)
        return target

if __name__ == '__main__':
    #input = sys.stdin.read()
    #nums = list(map(int, input.split()))

    nums = [0,1,2,3,4]
    index = [0,1,2,2,1]
    sol = Solution()
    sol.createTargetArray(nums, index)
