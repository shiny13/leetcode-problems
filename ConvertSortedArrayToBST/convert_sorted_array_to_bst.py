import sys 
from typing import List 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def fn(lo, hi):
            """Return BST using nums[lo:hi]"""
            if lo == hi: return None
            mid = (lo + hi)//2
            return TreeNode(nums[mid], fn(lo, mid), fn(mid+1, hi))
        
        return fn(0, len(nums))

if __name__ == '__main__':
    """
    node = TreeNode(0)
    node.left = TreeNode(-3)
    node.left.left = TreeNode(-10)
    node.right = TreeNode(9)
    node.right.right = TreeNode(5)
    """
    input = sys.stdin.read().strip()
    data = list(map(int, input.split()))

    sol = Solution()
    sol.sortedArrayToBST(data)
