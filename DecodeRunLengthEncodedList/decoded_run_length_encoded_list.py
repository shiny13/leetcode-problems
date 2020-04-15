import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    nums = list(map(int, input.split()))

    i = 0
    output = []
    while i < len(nums):
        output.extend(nums[i] * [nums[i+1]])
        i += 2
    print(output)
    #return output