import sys 
from random import randint

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = {}
        self.e = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.s:
            return False 
        self.s[val] = len(self.e)
        self.e.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.s:
            return False 
        ind = self.s[val]
        self.e[ind], self.e[-1] = self.e[-1], self.e[ind]
        self.s[self.e[ind]] = ind 
        self.e.pop()
        del self.s[val]
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        _rand = randint(0, len(self.e)-1)
        return self.e[_rand]
        
if __name__ == '__main__':
    # Your RandomizedSet object will be instantiated and called as such:
    randomSet = RandomizedSet()
    randomSet.insert(1)
    randomSet.insert(2)
    randomSet.getRandom()
    randomSet.remove(1)
    randomSet.insert(2)
    randomSet.getRandom()
