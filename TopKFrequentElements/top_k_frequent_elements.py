import sys 
from typing import List 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 1 and len(nums) == 1: 
            return nums
        output = []
        dic = {} 
        for i in nums:
            if i in dic:
                val = dic.get(i)
                val += 1
                dic.update({ i: val })
            else:
                dic[i] = 1
        s = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        x = 0
        for m, n in s:
            x += 1
            output.append(m)
            if x == k:
                break
        return output

if __name__ == '__main__':
    nums, k = [1,1,1,2,2,3], 2
    #nums, k = [1], 1

    sol = Solution()
    print(sol.topKFrequent(nums, k))
