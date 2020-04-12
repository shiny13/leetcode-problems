import sys 

if __name__ == '__main__':
    input = sys.stdin.read()
    nums = list(map(int, input.split()))
    nums.sort()
    i = 0
    output = 0
    while i < len(nums):
        output += min(nums[i], nums[i+1])
        i+=2
    print(output)
    #return output