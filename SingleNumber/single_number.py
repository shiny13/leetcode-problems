import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    print(data)
    items = {}
    for i in range(len(data)):
        if data[i] not in items:
            items[data[i]] = 1
        elif data[i] in items:
            items.pop(data[i], None)
    print(list(items.keys())[0])

#Solution with bit operation and O(1) space complexity
"""
class Solution(object):
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a
"""