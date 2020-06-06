import sys
from typing import List 

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        length = len(people)
        if length == 0:
            return []
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        #print(people)
        lis = []
        for p in people:
            lis.insert(p[1], p)
            #print(lis)

        return lis 

if __name__ == '__main__':
    data = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

    sol = Solution()
    print(sol.reconstructQueue(data))

