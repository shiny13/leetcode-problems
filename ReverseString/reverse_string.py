import sys 
from typing import List 

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        while i < int(len(s)//2):
            temp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = temp
            i += 1
        print(s)

if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = list(input)

    #data = ['H', 'e','l','l','o']
    data = ['L','i','o','n']
    sol = Solution()
    sol.reverseString(data)