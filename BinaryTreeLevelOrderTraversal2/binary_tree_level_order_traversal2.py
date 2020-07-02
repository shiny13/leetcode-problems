import sys 
from typing import List 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.levels = []
        if root == None:
            return []
        
        stack = [root]
        
        while stack:
            next_level_nodes = []
            current_lvl = []
            for node in stack:
                current_lvl.append(node.val)
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            stack = next_level_nodes
            self.levels.insert(0, current_lvl)
        return self.levels

if __name__ == '__main__':
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)

    sol = Solution()
    print(sol.levelOrderBottom(node))    
