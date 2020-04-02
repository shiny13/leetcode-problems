import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    nums = list(map(int, input.split()))
    items = {}
    for i in range(len(nums)):
        if nums[i] not in items:
            items[nums[i]] = 1
        elif nums[i] in items:
            items.pop(nums[i], None)
    print(list(items.keys()))
