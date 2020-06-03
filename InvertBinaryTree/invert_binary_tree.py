import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        def traverse(node: TreeNode):
            if node is None or node.val is None:
                return 
            tempRight = node.right 
            node.right = node.left 
            node.left = tempRight

            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return root