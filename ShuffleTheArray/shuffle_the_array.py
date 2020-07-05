import sys 
from typing import List 

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        counter = 1
        while counter <= n:
            output.append(nums[counter-1])
            output.append(nums[n+counter-1])
            counter += 1
        return output

if __name__ == '__main__':

    sol = Solution()
    sol.shuffle([2,5,1,3,4,7], 3)
    #sol.shuffle([1,2,3,4,4,3,2,1], 4)
    #sol.shuffle([1,1,2,2], 2)