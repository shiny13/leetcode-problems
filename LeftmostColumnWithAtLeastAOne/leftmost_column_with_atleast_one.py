import sys

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dim = binaryMatrix.dimensions()
        print(dim)
        value = -1
        y = dim[1]-1
        x = dim[0]-1
        while y >= 0:
            while x >= 0:
                _val = binaryMatrix.get(x,y)
                print("x {} y {} val {}".format(x,y,_val))
                if _val == 1:
                    value = y
                    break
                x-=1
            y-=1
        return value

