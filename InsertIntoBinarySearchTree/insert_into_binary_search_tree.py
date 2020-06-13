import sys 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        def insert(node: TreeNode, val: int):
            if node is None:
                node = TreeNode(val) 
                return
            if node.val is None:
                node.val = val 
                return

            if node.val > val and node.left is None:
                node.left = TreeNode(val)
                return
            elif node.val > val and node.left is not None:
                insert(node.left, val)
            
            if node.val < val and node.right is None:
                node.right = TreeNode(val)
                return
            elif node.val < val and node.right is not None:
                insert(node.right, val)

        insert(root, val)
        return root 
        """
        def recur(u):
            if not u: 
                return TreeNode(val)
            if val < u.val: 
                u.left  = recur(u.left)
            else:           
                u.right = recur(u.right)
            return u
        return recur(root)
"""
if __name__ == '__main__':
    
    sol = Solution()
"""