import sys
from typing import List 

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:

        target.sort()
        arr.sort()
        for i in range(len(target)):
            if target[i] != arr[i]:
                return False

        return True 

if __name__ == '__main__':
    target, arr = [1,2,3,4], [2,4,1,3]
    print(sol = Solution(target, arr))

