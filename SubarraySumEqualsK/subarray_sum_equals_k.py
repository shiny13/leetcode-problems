import sys
from typing import List 
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        our_sum = 0
        num_sub_arrays = 0
        for v in nums:
            our_sum += v
            if our_sum == k:
                num_sub_arrays += 1
            if (our_sum - k) in sums:
                num_sub_arrays += sums[our_sum-k]
            sums[our_sum] += 1
        print(num_sub_arrays)
        print(sums)
        return num_sub_arrays

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    nums = data[:-1]
    k = data[len(data)-1]
    
    sol = Solution()
    sol.subarraySum(nums,k)