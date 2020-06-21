import sys 
from typing import List 

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                output.append(idx+1)
            nums[idx] = -nums[idx]
            print(nums)

        return output

if __name__ == '__main__':
    input = sys.stdin.read().strip()
    data = list(map(int, input.split()))
    print(data)
    sol = Solution()
    print(sol.findDuplicates(data))
