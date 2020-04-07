import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    arr = list(map(int, input.split()))

    nums = {}
    for i in arr:
        if i in nums:
            item = nums.get(i, 0)
            item+=1
            nums.update({ i: item })
        else:
            nums[i] = 1
    counter = 0
    for key in nums:
        _next = key+1
        if _next not in nums:
            continue
        counter += nums[key]
    print(counter)
    #return counter
