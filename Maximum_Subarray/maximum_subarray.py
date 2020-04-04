import sys

def kadane(nums):
    max_current = nums[0]
    max_global = nums[0]
    if (len(nums) == 1):
        return max_global

    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        if max_current >= max_global:
            max_global = max_current
    return max_global

if __name__ == '__main__':
    input = sys.stdin.read()
    nums = list(map(int, input.split()))
    print(kadane(nums))