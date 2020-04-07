# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def traverse(t1, t2, t3):
            if t1 is None and t2 is None:
                return
            if t1.val is None and t2.val is None:
                return
            if (t1 is None or t1.val is None) and t2.val is not None:
                t3.val = t2.val
            elif (t2 is None or t2.val is None) and t1.val is not None:
                t3.val = t1.val
            else:
                t3.val = t1.val + t2.val 
            t3.left = TreeNode(None)
            t3.right = TreeNode(None)
            traverse(t1.left, t2,left, t3.left)
            traverse(t1.right, t2,right, t3.right)
        
        t3 = TreeNode(None)
        traverse(t1,t2,t3)
        return t3
"""
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1: return t2
        if t2: 
            t1.val = t1.val + t2.val 
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        return t1