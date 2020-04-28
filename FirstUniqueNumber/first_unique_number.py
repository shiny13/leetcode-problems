import sys 
from typing import List 

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.deque = []
        self.cache = {} 
        self.uniqueIndex = -1
        for i in range(len(nums)):
            self.deque.append(nums[i])
            if nums[i] in self.cache:
                self.cache.update({ nums[i]: False})
                if self.uniqueIndex > -1 and nums[i] == self.deque[self.uniqueIndex]:
                    self.findNextUnique()
            else:
                self.cache[nums[i]] = True
                if self.uniqueIndex == -1:
                    self.uniqueIndex = i
                else:
                    self.findNextUnique()

    def showFirstUnique(self) -> int:
        if self.uniqueIndex == -1:
            print(-1)
            return -1
        print(self.deque[self.uniqueIndex])
        return self.deque[self.uniqueIndex]

    def add(self, value: int) -> None:
        self.deque.append(value)
        if value in self.cache:
            self.cache.update({ value: False })
            if self.uniqueIndex > -1 and value == self.deque[self.uniqueIndex]:
                self.findNextUnique()
        else:
            self.cache[value] = True
            if self.uniqueIndex == -1:
                self.uniqueIndex = len(self.deque)-1
            else: 
                self.findNextUnique()

    def findNextUnique(self) -> None:
        found = False
        for i in range(self.uniqueIndex, len(self.deque)):
            val = self.cache.get(self.deque[i])
            if val:
                self.uniqueIndex = i
                found = True
                break
        if not found:
            self.uniqueIndex = -1


if __name__ == '__main__':
    input = sys.stdin.read()
    nums = list(map(int, input.split()))
    # Your FirstUnique object will be instantiated and called as such:
    obj = FirstUnique(nums)
    param_1 = obj.showFirstUnique()
    obj.add(5)
    obj.showFirstUnique()
    obj.add(2)
    obj.showFirstUnique()
    obj.add(3)
    obj.showFirstUnique()