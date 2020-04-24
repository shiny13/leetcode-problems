import sys
from collections import deque

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.deque = deque()
        self.cache = {}   
    def get(self, key):
        if key in self.cache:
            val = self.cache[key]
            self._remove(key)
            self.deque.append((key,val))
            return val
        return -1
    def put(self, key, value):
        if key in self.cache:
            self._remove(key)
        self.deque.append((key,value))
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            k, v = self.deque.popleft()
            del self.cache[k]
    def _remove(self, key):
        for k, v in self.deque:
                if k == key:
                    self.deque.remove((k, v))
                    break

# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)
#param_1 = obj.get(key)
"""
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)        #returns 1
cache.put(3, 3)    #evicts key 2
cache.get(2)       #returns -1 (not found)
cache.put(4, 4)    #evicts key 1
cache.get(1)       #returns -1 (not found)
cache.get(3)       #returns 3
cache.get(4)       #returns 4
"""
cache.get(2)
cache.put(2,6)
cache.get(1)
cache.put(1,5)
cache.put(1,2)
cache.get(1)
cache.get(-1)