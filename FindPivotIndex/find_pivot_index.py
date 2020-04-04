import sys

def pivotIndex(nums):
    S = sum(nums)
    leftsum = 0
    for i, x in enumerate(nums):
        if leftsum == (S - leftsum - x):
            return i
        leftsum += x
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    nums = list(map(int, input.split()))
    print(pivotIndex(nums))