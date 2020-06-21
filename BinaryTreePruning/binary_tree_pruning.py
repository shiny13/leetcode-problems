import sys 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def prune(node: TreeNode):
            if not node: return False 
            a1 = prune(node.left)
            a2 = prune(node.right)
            if not a1: 
                node.left = None 
            if not a2:
                node.right = None 
            return node.val == 1 or a1 or a2 

        return root if prune(root) else None

if __name__ == '__main__':

    node = TreeNode(1)
    node.left = TreeNode(0)
    node.left.left = TreeNode(0)
    node.left.right = TreeNode(0)
    node.right = TreeNode(1)
    node.right.left = TreeNode(0)
    node.right.right = TreeNode(1)

    sol = Solution()
    sol.pruneTree(node)